from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField
from wtforms.validators import DataRequired


class RainbowForm(FlaskForm):
    input = IntegerField("Number of occurrences", validators=[DataRequired()])
    submit = SubmitField("Submit")
