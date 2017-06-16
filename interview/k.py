#!/usr/bin/env python
# coding=utf-8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def FindKthToTail(head, k):
    pnode = head
    length = 0
    nodeList = []
    while pnode:
        nodeList.append(pnode)
        pnode = pnode.next
        length += 1
    if k > length or length <= 0:
        return None

    return nodeList[length-k]


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    print(FindKthToTail(a, 6))
    print(FindKthToTail(a, 1).val)
