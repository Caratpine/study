# coding=utf-8

from flask import Flask, url_for, redirect, render_template
from flask_login import LoginManager, UserMixin, login_required, login_user
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)
app.secret_key = 'please-generate-a-random-secret_key'

login_mangager = LoginManager(app)
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))


class LoginForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Log In')


@login_mangager.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/')
@login_required
def index():
    return 'hello world'


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for('index'))
    return render_template('login.html', form=form)
