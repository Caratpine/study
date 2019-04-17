# coding=utf-8

import os
import socket


sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.bind('/tmp/python_unix_socket.sock')

while True:
    data = sock.recv(1024)

    if not data:
        continue

    print('-' * 20)
    print(data.decode('utf-8'))

    if "exit" == data.decode('utf-8'):
        break


sock.close()
os.remove('/tmp/python_unix_socket.sock')
print('Done')
