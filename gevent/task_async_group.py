# coding=utf-8

import gevent
from gevent import getcurrent
from gevent.pool import Group


group = Group()


def hello_from(n):
    print(f'Size of group {len(group)}')
    print(f'Hello from Greenlet {id(getcurrent())}')


group.map(hello_from, range(3))


def intensive(n):
    gevent.sleep(3 - n)
    return 'task', n


print('Ordered')

ogroup = Group()

for i in ogroup.imap(intensive, range(3)):
    print(i)

print('Unorderer')

igroup = Group()

for i in igroup.imap_unordered(intensive, range(3)):
    print(i)
