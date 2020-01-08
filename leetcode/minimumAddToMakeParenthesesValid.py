# coding=utf-8


class Solution(object):
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        num = 0
        for s in S:
            if s == '(':
                stack.append(s)
            if s == ')':
                if len(stack) == 0:
                    num += 1
                else:
                    stack.pop()
        while stack:
            stack.pop()
            num += 1
        return num
