# coding=utf-8

import argparse

parser = argparse.ArgumentParser(description='hello world')
parser.add_argument('--host', default='127.0.0.1', help='Host to listen on.')
parser.add_argument('--port', '-p', default=8080, type=int, help='Port to listen on.')
parser.add_argument('--workers', '-w', default=5, type=int, help='Number of workers to spawn.')
parser.add_argument('--app', dest='module', help='Web application')

args = parser.parse_args()
print(args.host)
print(args.module)
