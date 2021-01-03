<div align="center">
    <img src="https://cdn3.iconfinder.com/data/icons/party-fill-recreation-story/512/Dancing-512.png" alt="logo" height="196">
</div>

# dancing-lights

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)

A Python application to use Philips Hue bridge/lights for wiggling and jiggling

## Environment

- Python 3.7.9

## Usage

1. create virtualenv
2. activate virtualenv
3. update pip and setuptools
4. install deps
5. create a `.env` file and store the Philips Hue bridge's ip address

   ```
   # .env
   IP="x.x.x.x"
   ```

6. connect to the bridge (press the link button before running the script for the first time)
7. run the python app

Use `pip install -r requirements-dev.txt` for development.
It will install `pylint` and `black` to enable linting and auto-formatting.

## Example

### Windows

    python -m venv venv
    .\venv\Scripts\activate
    python -m pip install -U pip setuptools
    pip install -r requirements.txt
    python connect.py
    python app.py

### Linux

    python -m venv venv
    source venv/bin/activate
    python -m pip install -U pip setuptools
    pip install -r requirements.txt
    python connect.py
    python app.py

<hr>

<sup>

## Credits

- [Icon][1] by [Chanut is Industries][2]

</sup>

[1]: https://www.iconfinder.com/icons/7149745/dancing_dancer_party_lifestyle_happiness_entertainment_recreation_icon
[2]: https://www.iconfinder.com/Chanut-is
