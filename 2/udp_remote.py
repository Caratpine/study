import argparse, random, socket, sys

MAX_BYTES = 65535


def server(interface, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print("Listening at", sock.getsockname())
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        if random.random() < 0.5:
            print("Pretending to drop packet from {}".format(address))
            continue
        text = data.decode('ascii')
        print("The client at {} says {!r}".format(address, text))
        message = 'Your data was {} bytes long'.format(len(data))
        sock.sendto(message.encode('ascii'), address)


def client(hostname, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    hostname = sys.argv[2]
    sock.connect((hostname, port))
    print("Client socket name is {}".format(sock.getsockname()))

    delay = 0.1
    text = 'This is another message'
    data = text.encode('ascii')
    while True:
        sock.send(data)
        print("Waiting up to {} seconds for a reply".format(delay))
        sock.settimeout(delay)
        try:
            data = sock.recv(MAX_BYTES)
        except socket.timeout:
            delay *= 2
            if delay > 0.8:
                raise RuntimeError('I think the server is down')
        else:
            break
    print("The server says {!r}".format(data.decode('ascii')))


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060)
    parser.add_argument('host', help="hello wolr")
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)