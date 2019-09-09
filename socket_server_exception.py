# coding=utf-8

import socket
import time
import sys


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 8484))
    sock.listen(1024)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while True:
        client, addr = sock.accept()
        while True:
            data = client.recv(1024)
            if len(data) == 0:
                print('client closed')

            time.sleep(5)

            l = client.send(data)
            print(f'send bytes {l}')
            if l < 0:
                print('error write')

if __name__ == '__main__':
    main()
