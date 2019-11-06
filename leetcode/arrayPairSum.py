from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)
        s = 0
        for i in range(0, len(nums), 2):
            print(i)
            s += nums[i]
        return s

