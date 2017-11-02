import gevent
import random


def foo():
    print("Running in foo")
    gevent.sleep(0)
    print("Explicit context switch to foo again")


def bar():
    print("Explicit context to bar")
    gevent.sleep(0)
    print("Implicit context switch to bar")


def task(pid):
    print("task %s start" % pid)
    gevent.sleep(random.randint(0, 2) * 0.001)
    print("task %s done" % pid)


def syn():
    for i in range(1, 10):
        task(i)


def asyn():
    threads = [gevent.spawn(task, i) for i in range(10)]
    gevent.joinall(threads)


syn()

print('----')
asyn()
