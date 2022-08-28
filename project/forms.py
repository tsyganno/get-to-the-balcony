from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Email, Length, InputRequired


class ProfileForm(FlaskForm):
    side_of_the_world = StringField('Выберите сторону света, в которую желаете отправиться.', validators=[Length(max=32, min=0), InputRequired()])
    step = IntegerField('Как далеко планируете продвинуться?', validators=[InputRequired()])
    submit = SubmitField('Принять')
