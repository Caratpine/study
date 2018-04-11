# coding=utf-8

import socket

target_host = '127.0.0.1'
target_port = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((target_host, target_port))
client_socket.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")

response = client_socket.recv(4096)

print response
