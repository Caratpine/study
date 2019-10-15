# coding=utf-8

import copy


class Solution:
    def permute(self, nums):
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
