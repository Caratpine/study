# coding=utf-8

import os

a = {}
pid = os.fork()
if pid == 0:
    a['a'] = 1
    print(a, f'child: {os.getpid()}')

a['b'] = 1
print(a, f'pid: {os.getpid()}')
