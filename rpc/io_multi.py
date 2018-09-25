# coding=utf-8

import sys
import time
import queue
import select
import socket
import logging


g_select_time = 10


class Server(object):
    def __init__(self, host='localhost', port=8989, timeout=2.0, client_nums=10):
        self.host = host
        self.port = port
        self.timeout = timeout,
        self.client_nums = client_nums
        self.buffer_size = 1024

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setblocking(False)
        self.server.settimeout(2.0)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)

        self.server.bind((self.host, port))
        self.server.listen(10)

        self.inputs = [self.server]
        self.outputs = []
        self.message_queues = {}
        self.client_info = {}

    def run(self):
        while True:
            read_list, write_list, error_list = select.select(self.inputs, self.outputs, self.inputs, 10)
            if not (read_list or write_list or error_list):
                continue

            for s in read_list:
                if s is self.server:
                    sock, addr = s.accept()
                    print('%s connect.' % addr)
                    sock.setblocking(0)
                    self.inputs.append(sock)
                    self.client_info[sock] = str(addr)
                    self.message_queues[sock] = queue.Queue()
                else:
                    try:
                        data = s.recv(1024)
                    except Exception:
                        data = ''
                        logging.error('Client error')
                    if data:
                        data = '%s %s say: %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), self.client_info[s], data)
                        self.message_queues[s].put(data)

                        if s not in self.outputs:
                            self.outputs.append(s)
                    else:
                        print('Client: %s close.' % self.client_info[s])
                        if s in self.outputs:
                            self.outputs.remove(s)
                        self.inputs.remove(s)
                        s.close()
                        del self.message_queues[s]
                        del self.client_info[s]

            for s in write_list:
                next_msg = 'fuck'
                try:
                    next_msg = self.message_queues[s].get_nowait()
                except queue.Empty:
                    logging.error('Output queue is empty')
                    self.outputs.remove(s)
                except Exception as e:
                    err_msg = 'Send Data Error! ErrMsg: %s' % e
                    logging.error(err_msg)
                    if s in self.outputs:
                        self.outputs.remove(s)

                if s is not self.server:
                    try:
                        s.sendall(next_msg)
                    except Exception as e:
                        err_msg = "Send Data to %s  Error! ErrMsg: %s" % (self.client_info[s], e)
                        logging.error(err_msg)
                        if s in self.inputs:
                            self.inputs.remove(s)
                            s.close()
                        if s in self.outputs:
                            self.outputs.remove(s)
                        if s in self.message_queues:
                            del self.message_queues[s]
                        del self.client_info[s]

            for s in error_list:
                logging.error("Client:%s Close Error." % str(self.client_info[cli]))
                if s in self.inputs:
                    self.inputs.remove(s)
                    s.close()
                if s in self.outputs:
                    self.outputs.remove(s)
                if s in self.message_queues:
                    del self.message_queues[s]
                del self.client_info[s]


if __name__ == '__main__':
    Server().run()
