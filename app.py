import os
import time
from multiprocessing import Process

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from phue import Bridge
from whitenoise import WhiteNoise


from forms import RainbowForm
from settings import ip_address
from utils import rgb_to_xy

app = Flask(__name__)
Bootstrap(app)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "SECRET_KEY")
app.config["BOOTSTRAP_SERVE_LOCAL"] = True


b = Bridge(ip_address)

lights = b.get_light_objects()

colors = [
    (148, 0, 211),
    (75, 0, 130),
    (0, 0, 255),
    (0, 255, 0),
    (255, 255, 0),
    (255, 127, 0),
    (255, 0, 0),
]


def make_rainbow(times):

    for i in range(times * len(colors)):

        for light in lights:

            color = [v / 255 for v in colors[i % len(colors)]]
            xy = rgb_to_xy(*color)
            light.transitiontime = 5
            light.xy = xy

        time.sleep(0.5)

    print("done looping")


@app.route("/", methods=["get", "post"])
def index():
    form = RainbowForm(request.form)

    if request.method == "POST":
        rainbow_process = Process(
            target=make_rainbow,
            args=(form.input.data,),
            daemon=True,
        )
        rainbow_process.start()

    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
