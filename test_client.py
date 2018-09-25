# coding=utf-8

import gevent
import struct
from gevent.server import StreamServer
from socketpool import ConnectionPool, TcpConnector


def echo(sock, address):
    print('New connection from %s:%s' % address)
    while True:
        data = sock.recv(1024)
        if not data:
            break
        sock.send(data)
        print('echoed %r' % data)


if __name__ == '__main__':
    import time
    options = {'host': 'localhost', 'port': 6000}
    pool = ConnectionPool(factory=TcpConnector, backend='gevent')
    server = StreamServer(('localhost', 6000), echo)
    gevent.spawn(server.serve_forever)

    def run_pool(data):
        print('ok')
        with pool.connection(**options) as conn:
            print('sending')
            # data = struct.pack('s', data)
            sent = conn.send(data)
            print('send %d bytes' % sent)
            echo_data = conn.recv(1024)
            # echo_data = struct.unpack('s', echo_data)
            print('got %s' % data)
            assert data == echo_data

    start = time.time()
    jobs = [gevent.spawn(run_pool, b'hello world') for _ in range(20)]
    gevent.joinall(jobs)
    delay = time.time() - start
    print(delay)
