# coding=utf-8

from config import h


@h.task()
def count_beans(num):
    print(f'-- counted {num} beans --')



