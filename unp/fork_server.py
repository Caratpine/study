# coding=utf-8

import os
import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 6754))
    sock.listen(1024)

    pid = os.fork()

    if pid > 0:
        print('parent')
        while True:
            client, addr = sock.accept()
            print('parent', addr)
    elif pid == 0:
        print('child')
        while True:
            client, addr = sock.accept()
            print('child', addr)
    else:
        print('error')


if __name__ == '__main__':
    main()
