# coding=utf-8

import socket
from shadowsocks.encrypt import Encryptor

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('0.0.0.0', 8388))

encryptor = Encryptor('123456', 'aes-256-cfb')
data = encryptor.encrypt(b'hello world')

sock.sendall(data)
