from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
