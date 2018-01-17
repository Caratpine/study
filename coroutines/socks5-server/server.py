# coding=utf-8

import asyncio
import logging
import struct
import socket


loop = asyncio.get_event_loop()


class Client(asyncio.Protocol):
    def connection_made(self, transport):
        self.connected = True
        self.transport = transport

    def data_received(self, data):
        logging.info("receive data with length: {}".format(len(data)))
        self.server_transport.write(data)

    def connection_lost(self, *args):
        self.connected = False
        self.server_transport.close()


class Server(asyncio.Protocol):
    STAGE_HELLO = 1
    STAGE_AUTH = 2
    STAGE_INIT = 3
    STAGE_WORK = 4

    CMD_CONNECT = 1
    CMD_BIND = 2
    CMD_UDP_ASSOCIATE = 3

    ATYP_IPV4 = 1
    ATYP_DOMAIN = 3
    ATYP_IPV6 = 4

    METHOD_NOAUTH = 0
    METHOD_USER = 2
    METHOD_NOAC = 0xff

    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        logging.info('connection from {}'.format(peername))
        self.stage = self.STAGE_HELLO
        self.transport = transport

    def data_received(self, data):
        if self.stage == self.STAGE_HELLO:
            self.handle_socks(data)
        elif self.stage == self.STAGE_AUTH:
            self.auth(data)
        elif self.stage == self.STAGE_INIT:
            ver, cmd, rsv, atyp = struct.unpack('!BBBB', data[0:4])

            if cmd == self.CMD_CONNECT:
                domain, port = self.parse_connect(atyp, data)
                self.waiter = asyncio.async(self.cmd_connect(domain, port))
                self.stage = self.STAGE_WORK
            elif cmd == self.CMD_BIND:
                pass
            else:
                raise NotImplementedError("Not implement {} yet!".format(cmd))
        elif self.stage == self.STAGE_WORK:
            logging.info('send data with length {}'.format(len(data)))
            asyncio.async(self.send_data(data))
        else:
            raise Exception("Unknown stage!!!")

    def handle_socks(self, data):
        ver, nmethods = struct.unpack('!BB', data[0:2])
        logging.info("version: {}, nmethods: {}".format(ver, nmethods))
        if ver != 5:
            raise Exception('Cannot recognize the protocol!')
        methods = struct.unpack('!' + 'B' * nmethods, data[2:2 + nmethods])
        logging.info('methods: {}'.format(methods))

        if self.METHOD_USER in methods:
            self.method = self.METHOD_USER
        elif self.METHOD_NOAUTH in methods:
            self.method = self.METHOD_NOAUTH
        else:
            self.method = self.METHOD_NOAC
        data_s = b'\05' + struct.pack('!B', self.method)
        self.transport.write(data_s)

        if self.method == self.METHOD_NOAC:
            self.transport.close()
            logging.info("No available authorizatrion method!")
            return
        if self.method == self.METHOD_NOAUTH:
            self.stage = self.STAGE_INIT
        else:
            self.stage = self.STAGE_AUTH
        logging.info('Authentication is complete!')

    @asyncio.coroutine
    def send_data(self, data):
        yield from self.waiter
        self._client.transport.write(data)

    @asyncio.coroutine
    def cmd_connect(self, domain, port):
        transport, client = yield from loop.create_connection(Client, domain, port)
        client.server_transport = self.transport
        self._client = client
        ip, port = transport.get_extra_info('sockname')

        data_s = b'\x05\x00\x00\x01'

        for i in ip.split('.'):
            data_s += struct.pack('!B', int(i))

        data_s += struct.pack('!H', port)
        self.transport.write(data_s)
        logging.info('connected to {}, {}'.format(domain, port))

    def parse_connect(self, atyp, data):
        cur = 4

        if atyp == self.ATYP_DOMAIN:
            domain_len = struct.unpack('!B', data[cur:cur + 1])[0]
            cur += 1
            domain = data[cur:cur + domain_len].decode()
            cur += domain_len
        elif atyp == self.ATYP_IPV4:
            domain = socket.inet_ntop(socket.AF_INET, data[cur:cur + 4])
            cur += 4
        elif atyp == self.ATYP_IPV6:
            domain = socket.inet_ntop(socket.AF_INET6, data[cur:cur + 16])
            cur += 16
        else:
            raise Exception("Unknown address type!")

        port = struct.unpack('!H', data[cur:cur + 2])[0]
        return domain, port
