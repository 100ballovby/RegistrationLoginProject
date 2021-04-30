from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import EqualTo
from wtforms.validators import InputRequired


class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя',
                           validators=[InputRequired()])
    password = StringField('Пароль', validators=[InputRequired(),
                                                 EqualTo(fieldname='password_again',
                                                         message='Passwords must be equal')])
    password_again = StringField('Пароль (еще раз)',
                                 validators=[InputRequired()])


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[InputRequired()])
    password = StringField('Пароль', validators=[InputRequired()])
