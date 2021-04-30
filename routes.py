from app import app, db, login
from flask import render_template, flash, redirect, request, url_for
from forms import RegisterForm, LoginForm
from models import User
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import current_user, login_user, logout_user, login_required


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/')
@login_required
def main_page():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm(request.form)
    if current_user.is_authenticated:
        return redirect(url_for('main_page'))

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):  # если пользователь есть в БД
            return redirect(url_for('login_page'))
        login_user(user)
        return redirect(url_for('main_page'))
    return render_template('login.html', form=form)


@app.route('/register', methods=['POST', 'GET'])
def register_page():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate:
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


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main_page'))