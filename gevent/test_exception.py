# coding=utf-8

import gevent


def win():
    return 'You win!'


def fail():
    raise Exception('You failed')


winner = gevent.spawn(win)
loser = gevent.spawn(fail)

print(winner.started)
print(loser.started)

try:
    gevent.joinall([winner, loser])
except Exception as e:
    print('fuck')

print(winner.ready())
print(loser.ready())

print(winner.value)
print(loser.value)

print(winner.successful())
print(loser.successful())


print(loser.exception)