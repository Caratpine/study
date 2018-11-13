# coding=utf-8

import gevent
from gevent.queue import Queue, Empty


tasks = Queue(maxsize=3)


def worker(n):
    try:
        while True:
            task = tasks.get(timeout=1)
            print(f'Worker {n} got task {task}')
            gevent.sleep(0)
    except Empty:
        print('Quit time')


def boss():
    for i in range(1, 10):
        tasks.put(i)
        print(f'boss put {i}')

    print('Assigned all work in iteration 1')

    for i in range(10, 20):
        print(f'boss put {i}')
        tasks.put(i)

    print('Assigned all work in iteration 2')


gevent.joinall([
    gevent.spawn(boss),
    gevent.spawn(worker, 'steve'),
    gevent.spawn(worker, 'john'),
    gevent.spawn(worker, 'bob'),
])