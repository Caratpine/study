#!/usr/bin/env python
# coding=utf-8

from collections import deque


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reversed(listNode):
    l = deque()
    if not listNode:
        return l
    node = listNode
    while node:
        l.appendleft(node.val)
        node = node.next
    return l


if __name__ == '__main__':
    a = ListNode(67)
    b = ListNode(0)
    c = ListNode(24)
    d = ListNode(58)
    a.next = b
    b.next = c
    c.next = d
