from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        stack = []
        for v in pushed:
            stack.append(v)
            while stack and stack[-1] == popped[i]:
                stack.pop()
                i += 1

        while stack:
            if stack[-1] == popped[i]:
                stack.pop()
                i += 1
            else:
                break

        return False if stack else True
