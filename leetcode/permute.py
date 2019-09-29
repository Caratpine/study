# coding=utf-8

import copy


class Solution:
    def permute(self, nums):
        def backtracking(nums, tmp):
            if len(nums) == len(tmp):
                results.append(copy.copy(tmp))
            else:
                for n in nums:
                    if n in tmp:
                        continue
                    tmp.append(n)
                    backtracking(nums, tmp)
                    tmp.pop()

        results = []
        tmp = []
        backtracking(nums, tmp)
        return results
