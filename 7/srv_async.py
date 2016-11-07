#!/usr/bin/env python3

import select, zen_utils


def all_events_forever(poll_object):
    while True:
        for fd, event in poll_object.poll():
            yield fd, event


def serve(listener):
    sockets = {listener.fileno(): listener}
    addresses = {}
    bytes_received = {}
    bytes_to_send = {}

    poll_object = select.poll()
    poll_object.register(listener, select.POLLIN)

    for fd, event in all_events_forever(poll_object):
        sock = sockets[fd]
        print("event::", event)

        if event & (select.POLLHUP | select.POLLERR | select.POLLNVAL):
            print("hhhh::", (event & (select.POLLHUP | select.POLLERR | select.POLLNVAL)))
            address = addresses.pop(sock)
            rb = bytes_received.pop(sock, b'')
            sb = bytes_to_send.pop(sock, b'')
            if rb:
                print("Client {} sent {} but then closed".format(address, rb))
            elif sb:
                print("Client {} closed before we send {}".format(address, sb))
            else:
                print("Client {} closed socket normally".format(address))
            poll_object.unregister(fd)
            del sockets[fd]

        elif sock is listener:
            sock, address = sock.accept()
            print("Accepted connection from {}".format(address))
            sock.setblocking(False)
            sockets[sock.fileno()] = sock
            print("1111sockfileno:", sock.fileno())
            addresses[sock] = address
            poll_object.register(sock, select.POLLIN)

        elif event & select.POLLIN:
            print("2222")
            more_data = sock.recv(4096)
            print(more_data)
            if not more_data:
                sock.close()
                continue
            data = bytes_received.pop(sock, b'') + more_data
            if data.endswith(b'?'):
                bytes_to_send[sock] = zen_utils.get_answer(data)
                poll_object.modify(sock, select.POLLOUT)
            else:
                bytes_received[sock] = data

        elif event & select.POLLOUT:
            print("3333")
            data = bytes_to_send.pop(sock)
            n = sock.send(data)
            if n < len(data):
                bytes_to_send[sock] = data[n:]
            else:
                poll_object.modify(sock, select.POLLIN)


if __name__ == '__main__':
    address = zen_utils.parse_command_line("low-level async server")
    listener = zen_utils.create_srv_socket(address)
    serve(listener)
