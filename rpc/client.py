# coding=utf-8

import time
import json
import socket
import struct


def rpc(sock, in_, params):
    request = json.dumps({'in': in_, 'params': params})
    length_prefix = struct.pack('I', len(request))
    sock.sendall(length_prefix)
    sock.sendall(request)
    length_prefix = sock.recv(4)
    length, _ = struct.unpack('I', length_prefix)
    body = sock.recv(length)
    response = json.loads(body)
    return response['out'], response['result']
