# coding=utf-8

import asyncio


loop = asyncio.get_event_loop()


class Client(asyncio.Protocol):
    def connection_made(self, transport):
        self.connected = True
        self.transport = transport

    def data_received(self, data):
        self.server_transport.write(data)

    def connection_lost(self, *args):
        self.connected = False
        self.server_transport.close()
