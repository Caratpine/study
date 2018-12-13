# coding=utf-8

from flask import Flask, jsonify
from flask_wtf.csrf import CSRFProtect
from webargs import fields
from webargs.flaskparser import use_kwargs


user_args = {
    'username': fields.Str(required=True),
    'password': fields.Str(validate=lambda p: len(p) >= 6),
    'display_per_page': fields.Int(missing=10),
    'languages': fields.DelimitedList(fields.Str(), missing='hello world')
}


csrf_protect = CSRFProtect()
app = Flask(__name__)
csrf_protect.init_app(app)


@app.route('/', methods=['POST'])
@csrf_protect.exempt
@use_kwargs(user_args)
def index(username, password, display_per_page, languages):
    print(username, password, display_per_page, languages)
    return jsonify(msg='hello world')


if __name__ == '__main__':
    app.run(debug=True, port=5555)

