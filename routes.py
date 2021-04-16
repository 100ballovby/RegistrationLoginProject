from app import app, db
from flask import render_template, flash, redirect, request, url_for
from forms import RegisterForm, LoginForm
from models import User
from werkzeug.security import check_password_hash, generate_password_hash


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
def register_page():
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        hashed_password = generate_password_hash(
            form.password.data,
            method='sha256')
        new_user = User(
            u=form.username.data,
            p=hashed_password
        )
        db.session.add(new_user)  # сохранить юзера в бд
        db.session.commit()  # применить изменения
        # если регистрация успешна, вернуться на главную страницу
        return redirect(url_for('main_page'))
    else:
        # показывать форму, когда заходят на страницу регистрации
        return render_template('register.html', form=form)

