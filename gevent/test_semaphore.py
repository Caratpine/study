# coding=utf-8

import gevent
from gevent.pool import Pool
from gevent.lock import BoundedSemaphore

sem = BoundedSemaphore()


def worker1(n):
    sem.acquire()
    print(f'Worker {n} acquired semaphore')
    gevent.sleep(0)
    sem.release()
    print(f'Worker {n} released semaphore')


def worker2(n):
    with sem:
        print(f'Worker {n} acquired semaphore')
        gevent.sleep(0)
    print(f'Worker {n} released semaphore')


pool = Pool()
pool.map(worker1, range(0, 2))
pool.map(worker2, range(3, 6))
