import json
import re
from urllib.parse import parse_qs, urlparse

import requests
import youtube_dl


def get_resources(videos):
    ydl_opts = {
        "writethumbnail": True,
        "outtmpl": "static/%(title)s - %(id)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            },
        ],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(videos)

    for video in videos:
        markup = requests.get(video).text

        base = "https://www.youtube.com/api/timedtext?v="
        rule = rf"\"{re.escape(base)}(.*?)\""

        part = re.findall(rule, markup)[-1]
        url = f"{base}{part}"
        url = url.replace(r"\u0026", "&") + "&fmt=json3"

        resp = requests.get(url).json()

        vid = parse_qs(urlparse(video).query)["v"][0]

        with open(f"static/{vid}.json", "w") as f:
            json.dump(resp, f)


if __name__ == "__main__":
    try:
        with open(".videos") as f:
            videos = [v.strip() for v in f.readlines()]

        get_resources(videos)
    except:
        print("Something went wrong.")
