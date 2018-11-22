# coding=utf-8

from flask import Flask
from flask_socketio import SocketIO



app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello world'

socket_io = SocketIO()

socket_io.init_app(app)


if __name__ == '__main__':
    app.run()
