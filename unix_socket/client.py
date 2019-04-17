# coding=utf-8

import os
import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.connect('/tmp/python_unix_socket.sock')

print('Ready')

while True:
    try:
        x = input('> ')
        if x != '':
            print('SEND: ', x)
            sock.send(x.encode('utf-8'))
            if x == 'exit':
                break

    except KeyboardInterrupt as k:
        sock.close()
        break
