from app import app
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError


class ContactForm(FlaskForm):
    name = StringField('Name',
    validators=[DataRequired()])
    email = StringField('E-mail',
    validators=[DataRequired(), Email()])
    message = TextAreaField('Message',
    validators=[DataRequired()])
    submit = SubmitField('Send Message')
