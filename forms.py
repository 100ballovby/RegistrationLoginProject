from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import EqualTo, DataRequired


class RegisterForm(FlaskForm):
    username = StringField('Имя пользователя',
                           validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired(),
                                                 EqualTo(fieldname='password_again',
                                                         message='Passwords must be equal')])
    password_again = PasswordField('Пароль (еще раз)',
                                 validators=[DataRequired()])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
