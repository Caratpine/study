# coding=utf-8

import gevent
from gevent.pool import Pool


pool = Pool(2)


def hello_from(n):
    print(n)
    print(f'Size of pool {len(pool)}')


pool.map(hello_from, range(1))
