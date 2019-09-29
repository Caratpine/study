# coding=utf-8

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        n = len(nums)

        def backtracking(j, tmp: List[int]):
            results.append(tmp)
            for i in range(j, n):
                backtracking(i + 1, tmp + [nums[i]])
        backtracking(0, [])
        return results
