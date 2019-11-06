from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if target <= n:
                return i
        return len(nums)
