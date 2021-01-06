import os
import time
from multiprocessing import Process
from pathlib import Path

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from phue import Bridge
from whitenoise import WhiteNoise


from settings import ip_address
from utils import rgb_to_xy, colors

app = Flask(__name__)
Bootstrap(app)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "SECRET_KEY")
app.config["BOOTSTRAP_SERVE_LOCAL"] = True


resources = dict(
    [
        (
            p.name.split(" - ")[-1].rstrip(".mp3"),
            (p.name, p.name.rstrip("mp3") + "webp"),
        )
        for p in Path("static").glob("*.mp3")
    ]
)


b = Bridge(ip_address)


def make_rainbow(times):
    lights = [l.light_id for l in b.get_light_objects()]

    for i in range(times * len(colors)):
        color = [v / 255 for v in colors[i % len(colors)]]
        xy = rgb_to_xy(*color)
        b.set_light(lights, "xy", xy)

        time.sleep(0.5)

    print("done looping")


@app.route("/", methods=["get"])
def index():
    return render_template("index.html", resources=resources)


@app.route("/listen/<vid>", methods=["get"])
def listen(vid):
    if vid == "rainbow":
        rainbow_process = Process(
            target=make_rainbow,
            args=(10,),
            daemon=True,
        )
        rainbow_process.start()
    else:
        pass

    return render_template("listen.html", vid=vid, resources=resources)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
