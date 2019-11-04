from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        rs = {}
        res = []
        nums.extend(nums)
        l = len(nums)
        for n in reversed(nums):
            while len(stack) > 0 and stack[-1] <= n:
                stack.pop()
            rs[n] = -1 if len(stack) == 0 else stack[-1]
            stack.append(n)

