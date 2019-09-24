# coding=utf-8

from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        start = len(sorted_nums)
        end = 0
        for idx, v in enumerate(nums):
            if nums[idx] != sorted_nums[idx]:
                start = min(start, idx)
                end = max(end, idx)
        return end - start + 1 if end - start >= 0 else 0
