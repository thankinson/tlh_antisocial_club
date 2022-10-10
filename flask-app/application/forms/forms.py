import email
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SignUpForm(FlaskForm):
    first_name = StringField('First Name: ', validators=[DataRequired(), Length(min=2, max=30)])
    last_name = StringField('Last Name: ', validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email: ', validators=[DataRequired(), Email(), Length(min=2)])
    passwd = PasswordField('Password: ', validators=[DataRequired()])
    confirm_passwd = PasswordField('Confirm Password: ', validators=[DataRequired(), EqualTo('passwd')])
    submit = SubmitField('Create Account')

class LoginForm(FlaskForm):
    email = StringField('Email: ', validators=[DataRequired(), Email(), Length(min=2)])
    passwd = PasswordField('Password: ', validators=[DataRequired()])
    submit = SubmitField('Login')