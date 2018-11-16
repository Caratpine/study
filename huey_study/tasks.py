# coding=utf-8

from datetime import datetime
from huey import crontab

from config import h


@h.task()
def count_beans(num):
    print(f'-- counted {num} beans --')
    return f'Counted {num} beans'


@h.task(retries=3, retry_delay=10)
def try_thrice():
    print(f'try... {datetime.now()}')
    raise Exception('nope')


@h.periodic_task(crontab(minute='*'))
def print_time():
    print(datetime.now())
