# coding=utf-8

import gevent
from gevent.queue import Queue

# q = Queue()
#
#
# def consumer(name):
#     while not q.empty():
#         print('%s got product %s' %(name, q.get()))
#         gevent.sleep(0)
#
#     print('%s Quit' % name)
#
#
# def producer():
#     for i in range(1, 10):
#         q.put(i)
#
#
# gevent.joinall([
#     gevent.spawn(producer),
#     gevent.spawn(consumer, 'xpb'),
#     gevent.spawn(consumer, 'xdd'),
#     gevent.spawn(consumer, 'fuck')
# ])


tasks = Queue()


def worker(n):
    while not tasks.empty():
        task = tasks.get()
        print('Worker %s got task %s' % (n, task))
        gevent.sleep(0)

    print('Quit time!')


def boss():
    for i in range(1, 25):
        tasks.put_nowait(i)


gevent.joinall([
    gevent.spawn(boss),
    gevent.spawn(worker, 'xpb'),
    gevent.spawn(worker, 'xdd'),
    gevent.spawn(worker, 'fuck')
])



