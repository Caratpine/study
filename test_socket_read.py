# coding=utf-8

import os
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 8084))
sock.listen(1024)
while True:
    client, addr = sock.accept()

    pid = os.fork()
    if pid > 0:
        data = b''
        while True:
            buffers = client.recv(5)
            print(f'father: {buffers}')
            if not buffers:
                print(f'father type {type(buffers)}')
                break
            data += buffers
        print(f'father: {data}')
        if data == b'':
            client.close()
        else:
            client.send(b'father ok')
            client.close()
    else:
        data = b''
        while True:
            buffers = client.recv(5)
            print(f'child: {buffers}')
            if not buffers:
                print(f'child type {type(buffers)}')
                break
            data += buffers
        print(f'child: {data}')
        if data == b'':
            client.close()
        else:
            client.send(b'child ok')
            client.close()

