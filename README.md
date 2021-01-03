# dancing-lights

![coding_style](https://img.shields.io/badge/code%20style-black-000000.svg)

## Environment

- Python 3.7.9

## Usage

1. create virtualenv
2. activate virtualenv
3. update pip and setuptools
4. install deps
5. run the python app

Use `pip install -r requirements-dev.txt` for development.
It will install `pylint` and `black` to enable linting and auto-formatting.

## Example

### Windows

    python -m venv venv
    .\venv\Scripts\activate
    python -m pip install -U pip setuptools
    pip install -r requirements.txt
    python app.py

### Linux

    python -m venv venv
    source venv/bin/activate
    python -m pip install -U pip setuptools
    pip install -r requirements.txt
    python app.py
