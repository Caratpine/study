# coding=utf-8

from flask import Flask
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy

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


@login_mangager.user_loader
def load_user(user_id):
    return User.get(user_id)
