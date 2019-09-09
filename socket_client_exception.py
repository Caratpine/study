# coding=utf-8

import time
import socket


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('0.0.0.0', 8484))

    while True:
        data = input()
        l = sock.send(data.encode('utf-8'))
        if l < 0:
            print('write failed')

        data = sock.recv(1024)
        if len(data) == 0:
            print('peer connection close\n')
        elif len(data) < 0:
            print('read failed')
        else:
            print(data)


if __name__ == '__main__':
    main()
