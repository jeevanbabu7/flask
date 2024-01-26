from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators  import Length,EqualTo,Email,DataRequired,ValidationError #importtant validators
from market.models import User

class RegisterForm(FlaskForm):

    def validate_username(self,user_to_check):  #cheacking whether username already exist or not 
        user = User.query.filter_by(username = user_to_check.data).first()
        if user:
            raise ValidationError('Username already exit! Please try different name')

    def validate_email_address(self,email_address_to_check): #check whther email exist or not 
        email_address  = User.query.filter_by(email_address = email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email address is already in use')

    username = StringField(label = 'Username' , validators = [Length(min = 2 ,max = 20),DataRequired()])
    email_address  = StringField(label = 'Email address' , validators = [Email(),DataRequired()])
    password1 = PasswordField(label = 'Password' , validators = [Length(min = 8) , DataRequired()])
    password2 = PasswordField(label = 'Confirm password',validators = [EqualTo('password1') ,DataRequired()]) 
    submit =SubmitField(label = 'Submit')


class LoginForm(FlaskForm):
    username = StringField(label = 'User name',validators = [DataRequired()])
    password = PasswordField(label = 'Password',validators = [DataRequired()])
    submit = SubmitField(label = 'Login')

    