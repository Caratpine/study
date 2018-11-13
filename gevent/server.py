# coding=utf-8

from gevent import socket, monkey, pool

monkey.patch_all()


def server(port, p):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', port))
    s.listen(5)

    while True:
        sock, addr = s.accept()
        p.spawn()


def handle_request(sock):
    try:
        while True:
            data = sock.recv(1024)
            print('recv:', data)
            sock.sendall(data)
            if not data:
                break
    except Exception as e:
        print(e)
    finally:
        sock.close()


if __name__ == '__main__':
    p = pool.Pool(5)
    server(8888, p)
