# coding=utf-8

from typing import List


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        prev = None
        curr = head

        while curr:
            tmp_node = curr.next
            curr.next = prev
            prev = curr
            curr = tmp_node

        stack = [prev.val]
        rs = [0]
        p = prev.next
        while p:
            while stack:
                if stack[-1] > p.val:
                    rs.append(stack[-1])
                    break
                stack.pop()
            if len(stack) == 0:
                rs.append(0)
            stack.append(p.val)
            p = p.next

        rs.reverse()
        return rs
