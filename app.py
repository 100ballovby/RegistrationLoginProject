from flask import Flask, render_template, flash, redirect, request, url_for
from forms import RegisterForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
app.config['SECRET_KEY'] = 'poprobui-ugadat'
app.config['SQLALCHEMY_DATABASE_URI'] = 'main.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
