from app import app
from flask import render_template, flash, redirect, request, url_for
from forms import RegisterForm, LoginForm
from werkzeug.security import check_password_hash, generate_password_hash


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/register')
def register_page():
    return render_template('register.html')

