# coding=utf-8

import socket
import pprint


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1.0)
sock.connect(('localhost', 9999))
sock.send(b'set a 123\r\n')
data = sock.recv(1024)


pprint.pprint(data)
sock.close()
