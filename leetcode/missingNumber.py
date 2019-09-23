# coding=utf-8


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        n = len(nums_set) + 1
        for v in range(n):
            if v not in nums_set:
                return v
        return 0
