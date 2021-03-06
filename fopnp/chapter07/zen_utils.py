#!/usr/bin/env/ python3

import time
import socket
import argparse

aphorisms = {b'Beautiful is better than?': b'Ugly.',
             b'Explicit is better than?': b'Implicit.',
             b'Simple is better than?': b'Complex.'}


def get_answer(aphorism):
    time.sleep(0.0)
    return aphorisms.get(aphorism, b'Error: unknown aphorism.')


def parse_command_line(description):
    """Parse command line and return a socket address."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    return address


def create_srv_socket(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(64)
    print("Listening at: {}".format(address))
    return sock


def accept_connections_forever(sock):
    while True:
        sc, address = sock.accept()
        print("Accept connection from {}".format(address))
        handle_conversation(sc, address)


def handle_conversation(sock, address):
    try:
        while True:
            handle_request(sock)
    except EOFError:
        print("Client socket to {} has closed".format(address))
    except Exception as e:
        print("Client {} error: {}".format(address, e))
    finally:
        sock.close()


def handle_request(sock):
    aphorism = recv_until(sock, b'?')
    answer = get_answer(aphorism)
    sock.sendall(answer)


def recv_until(sock, suffix):
    message = sock.recv(4096)
    if not message:
        raise EOFError('socket closed')
    while not message.endswith(suffix):
        data = sock.recv(4096)
        if not data:
            raise IOError('received {!r} then socket closed'.format(message))
        message += data
    return message
