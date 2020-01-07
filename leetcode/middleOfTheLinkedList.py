# coding=utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head: ListNode) -> ListNode:
        p1 = head
        p2 = head

        while True:
            if p2.next is None:
                return p1
            if p2.next.next is None:
                return p1.next
            p1 = p1.next
            p2 = p2.next.next

