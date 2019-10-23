from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        s = 0
        for v in ops:
            if v == 'C':
                top = stack.pop()
                s -= top
            elif v == 'D':
                n = 2 * stack[-1]
                s += n
                stack.append(n)
            elif v == '+':
                n = stack[-1] + stack[-2]
                s += n
                stack.append(n)
            else:
                s += int(v)
                stack.append(int(v))
        return s
