# coding=utf-8

from flask import Flask, jsonify
from flask_wtf.csrf import CSRFProtect
from webargs import fields, ValidationError
from webargs.flaskparser import use_kwargs, use_args


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
@use_args(user_args, locations=('json',))
def index(args):
    print(args)
    return jsonify(msg='hello world')


def must_exist_in_db(val):
    print('111')
    return True


def validate_db(val):
    print('222')
    raise ValidationError('error')


argmap = {
    'id': fields.Int(validate=[must_exist_in_db, validate_db])
}


@app.route('/test', methods=['POST'])
@csrf_protect.exempt
@use_args(argmap, locations=('json', ))
def test(args):
    print(args)
    return jsonify(msg='hello test')


if __name__ == '__main__':
    app.run(debug=True, port=5555)

