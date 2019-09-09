# coding=utf-8

import os


def child_handle():
    while True:
        pass


def main():
    p = 0
    for i in range(3):
        pid = os.fork()
        if pid == 0:
            break
        elif pid > 0:
            p = pid
        else:
            print('error')

    if p == 0:
        child_handle()
    else:
        while True:
            pass


if __name__ == '__main__':
    main()

