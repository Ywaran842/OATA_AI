from wtforms import StringField, PasswordField, validators, BooleanField
from flask_wtf import FlaskForm, RecaptchaField

class Loginform(FlaskForm):
    username = StringField('username', [validators.DataRequired(), validators.Length(min=4, max=25)])
    password = PasswordField('password', [validators.DataRequired(), validators.Length(min=4, max=25)])
    remember = BooleanField('remember', default=False)
    # recapcha = RecaptchaField()

class Registerform(FlaskForm):
    username = StringField('Username', [validators.DataRequired(), validators.Length(min=4, max=25)])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=8, max=25)])
    confirmpassword = PasswordField('Confirm Password', [validators.DataRequired(), validators.EqualTo('password')])
    emailid = StringField('Email', [validators.DataRequired(), validators.Length(min=10, max=25)])

