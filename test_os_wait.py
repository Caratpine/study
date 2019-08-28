# coding=utf-8

import os
import sys

def pr_exit(status: int) -> None:
    if os.WIFEXITED(status):
        print(f'normal termination, exit status = {os.WEXITSTATUS(status)}')
    elif os.WIFSIGNALED(status):
        print(f'abnormal termination, signal number = {os.WTERMSIG(status)} {os.WCOREDUMP(status)}')
    elif os.WIFSTOPPED(status):
        print(f'child stopped, signal number = {os.WSTOPSIG(status)}')


def main():
    pid = os.fork()
    if pid == 0:
        sys.exit(7)

    pid, status = os.wait()
    pr_exit(status)

    pid = os.fork()
    if pid == 0:
        os.abort()

    pid, status = os.wait()
    pr_exit(status)

    pid = os.fork()
    if pid == 0:
        a = 1 / 0

    pid, status = os.wait()
    pr_exit(status)

    sys.exit(0)


if __name__ == '__main__':
    main()
