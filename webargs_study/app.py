# coding=utf-8

from flask import Flask, jsonify, request
from webargs import fields, ValidationError
from webargs.flaskparser import use_kwargs, use_args, parser


user_args = {
    'username': fields.Str(required=True),
    'password': fields.Str(validate=lambda p: len(p) >= 6),
    'display_per_page': fields.Int(missing=10),
    'languages': fields.DelimitedList(fields.Str(), missing='hello world')
}


get_args = {
    'a': fields.Str(missing='hello')
}


app = Flask(__name__)


@app.route('/hello/<id>')
def hello_id(id):
    if __name__ == '__main__':
        payload = parser.parse(get_args, request)
    print(id, payload)
    return jsonify(id=id, payload=payload)


@app.route('/', methods=['POST'])
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
@use_args(argmap, locations=('json', ))
def test(args):
    print(args)
    return jsonify(msg='hello test')


if __name__ == '__main__':
    app.run(debug=True, port=5000)

