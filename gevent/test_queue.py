# coding=utf-8

import gevent
from gevent.queue import Queue

q = Queue()


def consumer(name):
    while not q.empty():
        print('%s got product %s' %(name, q.get()))
        gevent.sleep(0)

    print('%s Quit' % name)


def producer():
    for i in range(1, 10):
        q.put(i)


gevent.joinall([
    gevent.spawn(producer),
    gevent.spawn(consumer, 'xpb'),
    gevent.spawn(consumer, 'xdd'),
    gevent.spawn(consumer, 'fuck')
])
