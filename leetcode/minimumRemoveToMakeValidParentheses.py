# coding=utf-8


class Solution(object):
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        idx = []
        for i, v in enumerate(s):
            if v == '(':
                stack.append((v, i))
            if v == ')':
                if len(stack) == 0:
                    idx.append(i)
                elif stack[-1][0] == '(':
                    stack.pop()
        while stack:
            idx.append(stack.pop()[1])

        rs = []
        for i, v in enumerate(s):
            if i not in idx:
                rs.append(v)
        return ''.join(rs)
