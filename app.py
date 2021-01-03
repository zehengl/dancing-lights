import os

from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from whitenoise import WhiteNoise

from forms import SomeForm

app = Flask(__name__)
Bootstrap(app)
app.wsgi_app = WhiteNoise(app.wsgi_app, root="static/")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "SECRET_KEY")
app.config["BOOTSTRAP_SERVE_LOCAL"] = True


@app.route("/", methods=["get", "post"])
def index():
    form = SomeForm(request.form)

    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
