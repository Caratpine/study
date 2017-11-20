import logging
import socket
import select
import struct
# import selectors
import threading


def send_data(sock, data):
    bytes_sent = 0
    while True:
        r = sock.send(data[bytes_sent:])
        if r < 0:
            return r
        bytes_sent += r
        if bytes_sent == len(data):
            return bytes_sent


def handle_tcp(sock, remote):
    try:
        fdset = [sock, remote]
        while True:
            r, w, e = select.select(fdset, [], [])
            if sock in r:
                data = sock.recv(4096)
                if len(data) <= 0:
                    break
                result = send_data(remote, data)
                if result < len(data):
                    raise Exception("Failed to send all data")
            if remote in r:
                data = remote.recv(4096)
                if len(data) <= 0:
                    break
                result = send_data(sock, data)
                if result < len(data):
                    raise Exception("Failed to send all data")
    except Exception as e:
        raise(e)
    finally:
        sock.close()
        remote.close()


def handle_connect(sock, addr):
    sock.recv(256)
    sock.send(b'\x05\x00')
    data = sock.recv(4) or '\x00' * 4

    if data[1] != 1:
        sock.close()
        return

    addr_type = data[3]
    if addr_type == 1:
        addr_ip = sock.recv(4)
        remote_addr = socket.inet_ntoa(addr_ip)
    elif addr_type == 3:
        addr_len = int.from_bytes(sock.recv(1), byteorder='big')
        remote_addr = sock.recv(addr_len)
    elif addr_type == 4:
        addr_ip = sock.recv(16)
        remote_addr = socket.inet_ntop(socket.AF_INET6, addr_ip)
    else:
        sock.close()
        return

    remote_port = struct.unpack('>H', sock.recv(2))[0]
    reply = b'\x05\x00\x00\x01'
    reply += socket.inet_aton('0.0.0.0') + struct.pack('>H', 1080)
    sock.send(reply)

    logging.info("target--> {}:{}".format(remote_addr, remote_port))

    try:
        remote = socket.create_connection((remote_addr, remote_port))
        logging.info("connecting {}:{}".format(remote_addr, remote_port))
    except socket.error as e:
        logging.error("error: {}:{}, msg:{}".format(remote_addr, remote_port, e))
        sock.close()
        return

    handle_tcp(sock, remote)


def main():
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    socketServer.bind(('', 1080))
    socketServer.listen(5)

    # selector = selectors.DefaultSelector()
    # selector.register(socketServer, selectors.EVENT_READ, handle_connect)

    # while True:
    #     for key, event in selector.select():
    #         callback = key.data
    #         callback(key.fileobj)
    try:
        while True:
            sock, addr = socketServer.accept()
            t = threading.Thread(target=handle_connect, args=(sock, addr))
            t.start()
    except socket.error as e:
        logging.error(e)
    except KeyboardInterrupt:
        socketServer.close()


if __name__ == '__main__':
    main()
