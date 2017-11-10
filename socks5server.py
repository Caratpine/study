#!/usr/bin/env python3

import socket
import struct
import select
import selectors


srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_sock.bind(('127.0.0.1', 1080))
srv_sock.listen(1024)

print("Server listening on port:", 1080)


def handle_cli_connect(srv_sock):
    sock, address = srv_sock.accept()
    ver, methods = sock.recv(1), sock.recv(1)
    methods = sock.recv(ord(methods))

    sock.send(b'\x05\x00')

    ver, cmd, rsv, atype = sock.recv(1), sock.recv(1), sock.recv(1), sock.recv(1)

    assert ver == ver
    assert rsv == rsv

    if ord(cmd) is not 1:
        sock.close()
        return
    if ord(atype) == 1:
        remote_addr = socket.inet_ntoa(sock.recv(4))
        remote_port = struct.unpack(">H", sock.recv(2))[0]
    elif ord(atype) == 3:
        addr_len = ord(sock.recv(1))
        remote_addr = sock.recv(addr_len)
        remote_port = struct.unpack(">H", sock.recv(2))[0]
    else:
        reply = b"\x05\x08\x00\x01" + sock.inet_ntoa("0.0.0.0") + struct.pack(">H", 2222)
        sock.send(reply)
        sock.close()
        return

    print("cmd:{0} target ---> {1}:{2}".format(cmd, remote_addr, remote_port))

    remote_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    remote_sock.connect((remote_addr, remote_port))

    reply = b"\x05\x00\x00\x01" + socket.inet_aton("0.0.0.0") + struct.pack(">H", 2222)
    sock.send(reply)

    handle_tcp(sock, remote_sock)


def handle_tcp(cli_sock, remote_sock):
    print("pipping data...")
    try:
        fds = [cli_sock, remote_sock]
        while True:
            r, w, e = select.select(fds, [], [])
            if cli_sock in r:
                cli_data = cli_sock.recv(1024 * 100)
                if len(cli_data) <= 0:
                    break
                result = send_all(remote_sock, cli_data)
                if result < len(cli_data):
                    print("Fail pipping all data to target!!!")
                    break
            if remote_sock in r:
                remote_data = remote_sock.recv(1024 * 1000)
                if len(remote_data) <= 0:
                    break
                result = send_all(cli_sock, remote_data)
                if result < len(remote_data):
                    print("Failed pipping all data to client!!!")
                    break
    finally:
        cli_sock.close()
        remote_sock.close()
    print("piping data done.")


def send_all(sock, data):
    bytes_sent = 0
    while True:
        r = sock.send(data[bytes_sent:])
        if r < 0:
            return r
        bytes_sent += r
        if bytes_sent == len(data):
            return bytes_sent


selector = selectors.DefaultSelector()
selector.register(srv_sock, selectors.EVENT_READ, handle_cli_connect)


def loop():
    while True:
        poll = selector.select()
        for key, event in poll:
            callback = key.data
            callback(key.fileobj)


if __name__ == '__main__':
    loop()
