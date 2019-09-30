# coding=utf-8

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []

        def backtracking(tmp):
            if len(tmp) == len(nums):
                if tmp not in results:
                    results.append(tmp[:])
                return
            else:
                for n in nums:
                    if n in tmp:
                        continue
                    tmp.append(n)
                    backtracking(tmp)
                    tmp.pop()

        backtracking([])
        return results

