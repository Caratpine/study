# coding=utf-8

import select
import socket
from queue import Queue
from queue import Empty


def server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.bind(('0.0.0.0', 8999))
    sock.listen(2048)
    inputs = [sock]
    address_dict = {}
    print('start...')
    while True:
        r_fds, w_fds, e_fds = select.select(inputs, inputs, [], 5)
        if len(r_fds) != 0:
            for fds in r_fds:
                if fds is sock:
                    client, address = sock.accept()
                    client.setblocking(False)
                    inputs.append(client)
                    address_dict[client.fileno()] = address
                else:
                    data = fds.recv(1024)
                    if not data:
                        inputs.remove(fds)
                    else:
                        print(data)
        if len(w_fds) != 0:
            for fds in w_fds:
                address = address_dict[fds.fileno()]
                fds.send(f'{address}'.encode('utf-8'))


def server2():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.bind(('0.0.0.0', 8999))
    sock.listen(1024)
    inputs = [sock]
    outputs = []
    message_queues = {}

    while True:
        r_fds, w_fds, e_fds = select.select(inputs, outputs, inputs, 0)
        for fd in r_fds:
            if fd is sock:
                client, address = fd.accept()
                client.setblocking(False)
                inputs.append(client)
                message_queues[client] = Queue()
            else:
                data = fd.recv(1024)
                if data:
                    message_queues[fd].put(data)
                    if fd not in outputs:
                        outputs.append(fd)
                else:
                    if fd in outputs:
                        outputs.remove(fd)
                    inputs.remove(fd)
                    del message_queues[fd]
                    fd.close()
        for fd in w_fds:
            try:
                msg = message_queues[fd].get_nowait()
            except Empty:
                outputs.remove(fd)
            else:
                fd.send(msg)

        for fd in e_fds:
            inputs.remove(fd)
            if fd in outputs:
                outputs.remove(fd)
            del message_queues[fd]
            fd.close()


if __name__ == '__main__':
    server2()

