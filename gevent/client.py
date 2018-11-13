# coding=utf-8

import gevent
from gevent import socket, monkey

monkey.patch_all()


def client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('0.0.0.0', 8888))
    msg = b'this is gevent'
    s.sendall(msg)
    data = s.recv(1024)
    print('Received')
    s.close()


greenlets = []

for i in range(2000):
    greenlets.append(gevent.spawn(client))


gevent.joinall(greenlets)
