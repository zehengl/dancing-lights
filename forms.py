from flask_wtf import FlaskForm
from wtforms import SubmitField, TextField
from wtforms.validators import DataRequired


class SomeForm(FlaskForm):
    input1 = TextField("Input 1", validators=[DataRequired()])
    input2 = TextField("Input 2", validators=[DataRequired()])
    submit = SubmitField("Submit")
