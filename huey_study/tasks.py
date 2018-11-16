# coding=utf-8

from config import h


@h.task()
def count_beans(num):
    print(f'-- counted {num} beans --')
    return f'Counted {num} beans'


@h.task(retries=3)
def try_thrice():
    print('try...')
    raise Exception('nope')