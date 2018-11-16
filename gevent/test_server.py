# coding=utf-8

from gevent.server import StreamServer


def handle(sock, address):
    print(address)
    sock.send(b'Hello world')

    for i in range(5):
        sock.send(str(i).encode('utf-8'))
    sock.close()


server = StreamServer(('127.0.0.1', 7777), handle)
server.serve_forever()
