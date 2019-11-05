from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        l = len(nums)
        res = [-1 for n in range(l)]
        for n in reversed(list(range(0, l*2))):
            while len(stack) > 0 and stack[-1] <= nums[n % l]:
                stack.pop()
            res[n % l] = -1 if len(stack) == 0 else stack[-1]
            stack.append(nums[n % l])
        print(res)
        return res
