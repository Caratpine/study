# coding=utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        if head is None:
            return None
        while p.next is not None:
            if p.val == p.next.val:
                p.next = p.next.next
            if p.next is not None and p.val != p.next.val:
                p = p.next
        return head
