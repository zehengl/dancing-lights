<div align="center">
    <img src="https://cdn3.iconfinder.com/data/icons/party-fill-recreation-story/512/Dancing-512.png" alt="logo" height="196">
</div>

# dancing-lights

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)

A Python application to use Philips Hue bridge/lights for wiggling and jiggling

## Environment

- Python 3.9

## Usage

1. create virtualenv

   `python -m venv venv`

2. activate virtualenv

   `.\venv\Scripts\activate` on Windows or `source venv/bin/activate` on Linux

3. update pip and setuptools

   `python -m pip install -U pip setuptools`

4. install deps

   `pip install -r requirements.txt`

5. create a `.env` file and store the Philips Hue bridge's ip address

   ```
   # .env
   IP="x.x.x.x"
   ```

6. connect to the bridge (**press the link button before running the script for the first time**)

   `python connect.py`

7. run the python app

   `python app.py`

Use `pip install -r requirements-dev.txt` for development.
It will install `pylint` and `black` to enable linting and auto-formatting.

## Set Up Background Music for Lights

1. create a `.videos` file and store all the YouTube video links

   ```
   # .videos
   https://www.youtube.com/watch?v=9pkx51y4ppg
   https://www.youtube.com/watch?v=_6HzoUcx3eo
   ...
   ```

2. run the download script

   `python download.py`

   > It picks the last available cc from YouTube. So make sure that one is English.

## To-do

- [x] Display lyrics
- [ ] Control lights based on lyrics
- [ ] Configure Heroku buildpack for FFmpeg

<hr>

<sup>

## Credits

- [Icon][1] by [Chanut is Industries][2]

- [Rainbow image][3] from [https://wallpapers.gg/][4]

- [YouTube][5] videos

</sup>

[1]: https://www.iconfinder.com/icons/7149745/dancing_dancer_party_lifestyle_happiness_entertainment_recreation_icon
[2]: https://www.iconfinder.com/Chanut-is
[3]: https://wallpapers.gg/digital-rainbow-background-6k/
[4]: https://wallpapers.gg/
[5]: https://www.youtube.com/
