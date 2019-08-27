# coding=utf-8

import os
import select
import socket


def main():
    poll = select.epoll()


    poll = select.epoll()
    pid = os.fork()

    if pid == 0:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', 6754))
        sock.listen(1024)
        poll.register(sock.fileno(), select.EPOLLIN)

        while True:
            fds_ready = poll.poll(timeout=1.0)
            print(f'child: {fds_ready}')
    else:
        while True:
            fds_ready = poll.poll(timeout=1.0)
            print(f'father: {fds_ready}')


if __name__ == '__main__':
    main()
