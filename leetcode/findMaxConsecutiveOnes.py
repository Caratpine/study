from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = 0
        idx = 0
        nums.append(0)
        nums.insert(0, 0)
        for i, n in enumerate(nums):
            if n == 0:
                l = max(l, i - idx - 1)
                idx = i
        return l
