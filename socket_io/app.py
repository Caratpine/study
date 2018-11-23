# coding=utf-8

from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello world'

socket_io = SocketIO()

socket_io.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@socket_io.on('message', namespace='/test')
def handle_message(message):
    print(message)
    emit('connect', {'data': 'hello world'})





if __name__ == '__main__':
    app.run(debug=True, port=7777)
