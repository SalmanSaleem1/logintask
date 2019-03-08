from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_wtf.file import FileAllowed,FileField, FileRequired
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=25)])
    username = StringField('User Name', validators=[DataRequired(), Length(min=2, max=15)])
    email = StringField('Email', validators=[DataRequired(), Length(min=2, max=25), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=2, max=25)])
    confirm_password = PasswordField('Confirm Pasword', validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField('Submit')


class LoginForm(FlaskForm):
    email = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField('Login')


class AccountForm(FlaskForm):
    name = StringField(validators=[DataRequired(), Length(min=2, max=25)])
    username = StringField(validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField(validators=[DataRequired(), Length(min=2, max=35), Email()])
    picture = FileField('Upload Image', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    update = SubmitField('Update')
