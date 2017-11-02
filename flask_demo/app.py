#!/usr/bin/env python
# coding=utf-8

from flask import Flask, session, escape, request

app = Flask(__name__)
app.secret_key = 'please-generate-a-random-secret_key'


@app.route('/')
def index():
    if 'username' in session:
        return 'hello, {}'.format(escape(session['username']))
    return 'hello, stranger'


@app.route('/login', methods=['POST'])
def login():
    session['username'] = request.form['username']
    session['password'] = 'forever8023scr'
    return 'login success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
