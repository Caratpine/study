# coding=utf-8

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        nums = list(range(1, n + 1))

        def backtracking(j, tmp):
            if len(tmp) == k:
                results.append(tmp)
                return

            for i in range(j, n):
                backtracking(i + 1, tmp + [nums[i]])

        backtracking(0, [])
        return results


