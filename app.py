import json
import os
import time
from multiprocessing import Process
from pathlib import Path

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from phue import Bridge, PhueRegistrationException
from whitenoise import WhiteNoise


from settings import ip_address
from utils import rgb_to_xy, colors

app = Flask(__name__)
Bootstrap(app)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "SECRET_KEY")
app.config["BOOTSTRAP_SERVE_LOCAL"] = True


def get_lyrics(path):
    try:
        cc = json.loads(open(path).read())
    except:
        return []
    results = []
    for evt in cc.get("events", []):
        results.append(
            (
                evt.get("tStartMs", 0) / 1000.0,
                evt.get("dDurationMs", 0) / 1000.0,
                "".join([seg.get("utf8", "") for seg in evt.get("segs", [])]),
            )
        )
    return [r for r in results if r[-1].strip()]


def get_id(path):
    return path.name.split(" - ")[-1].rstrip(".mp3")


def get_image(path):
    return path.name.rstrip("mp3") + "webp"


def get_mp3(path):
    return path.name


resources = [
    (
        get_id(p),
        (get_mp3(p), get_image(p), get_lyrics(p.parent / f"{get_id(p)}.json")),
    )
    for p in Path("static").glob("*.mp3")
]

if ip_address:
    try:
        b = Bridge(ip_address)
    except PhueRegistrationException:
        b = None
        print("Your Philips Hue bridge is not set up properly.")
else:
    b = None
    print("No setting for your Philips Hue bridge")


def make_rainbow(b, times):
    if not b:
        print("nothing happens")
        return

    lights = [l.light_id for l in b.get_light_objects()]

    for i in range(times * len(colors)):
        color = [v / 255 for v in colors[i % len(colors)]]
        xy = rgb_to_xy(*color)
        b.set_light(lights, "xy", xy)

        time.sleep(0.5)

    print("done looping")


@app.route("/", methods=["get"])
def index():
    return render_template(
        "index.html",
        resources=dict([(vid, (mp3, image)) for vid, (mp3, image, _) in resources]),
    )


@app.route("/listen/<vid>", methods=["get"])
def listen(vid):
    if vid == "rainbow":
        rainbow_process = Process(
            target=make_rainbow,
            args=(b, 10),
            daemon=True,
        )
        rainbow_process.start()
    else:
        pass

    return render_template("listen.html", vid=vid, resources=dict(resources))


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
