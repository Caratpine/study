# coding=utf-8

import os
import sys
import time


def main():
    pid = os.fork()
    if pid == 0:
        print('child process')
        ppid = os.fork()
        if ppid > 0:
            sys.exit(0)
        time.sleep(3)
        print(f'second child, parent pid = {os.getppid()}')
        sys.exit(0)

    time.sleep(1)
    p, stat = os.waitpid(pid, 0)
    print(p, stat)
    if p == pid:
        sys.exit(0)
    else:
        print('wait pid error')


if __name__ == '__main__':
    main()
