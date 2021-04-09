from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import EqualTo
from wtforms.validators import InputRequired


class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя',
                           validators=[InputRequired()])
    password = StringField('Пароль',
                           validators=[InputRequired()])
    password_again = StringField('Пароль (еще раз)',
                                 validators=[InputRequired(),
                                             EqualTo('password')])


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[InputRequired()])
    password = StringField('Пароль', validators=[InputRequired()])
