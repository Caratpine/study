# coding=utf-8

import socket
from datetime import datetime
import threading


def client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('127.0.0.1', 8084))
    sock.send(f'hello world {datetime.now()}'.encode('utf-8'))
    data = sock.recv(1024)
    print(data.decode('utf-8'))
    sock.close()


if __name__ == '__main__':
    threads = []
    for i in range(1):
        t = threading.Thread(target=client)
        threads.append(t)
        t.daemon = True
        t.start()

    for t in threads:
        t.join()
