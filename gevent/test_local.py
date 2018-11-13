# coding=utf-8

import gevent
from gevent.local import local

stash = local()


def f1():
    stash.x = 1
    print(stash.x)


def f2():
    stash.y = 2
    stash.x = 3
    print(stash.y)

    try:
        print(stash.x)
    except AttributeError:
        print('x is not local to f2')


gevent.joinall([
    gevent.spawn(f1),
    gevent.spawn(f2)
])
