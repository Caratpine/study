from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        rs = {}
        num = []
        for v in reversed(nums2):
            while len(stack) > 0 and stack[-1] <= v:
                if stack[-1] <= v:
                    stack.pop()

            rs[v] = -1 if len(stack) == 0 else stack[-1]
            stack.append(v)

        for v in nums1:
            num.append(rs[v])
        return num
