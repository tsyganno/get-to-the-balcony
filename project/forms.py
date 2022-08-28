from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, Email, Length, InputRequired


class ProfileForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[Length(max=32, min=5), InputRequired()])
    password = PasswordField('Пароль', validators=[Length(max=24, min=9), InputRequired()])
    about_me = TextAreaField('О себе')
    submit = SubmitField('Принять')