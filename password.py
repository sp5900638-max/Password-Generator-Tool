from flask_wtf import FlaskForm
from wtforms import IntegerField,SubmitField,BooleanField
from wtforms.validators import DataRequired

class PasswordGenerator(FlaskForm):
    password=IntegerField("Password Length", validators=[DataRequired()])
    uppercase = BooleanField("Include Uppercase")
    lowercase = BooleanField("Include Lowercase")
    numbers = BooleanField("Include Numbers")
    symbols = BooleanField("Include Symbols")

    submit = SubmitField("Generate Password")
