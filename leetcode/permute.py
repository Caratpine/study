# coding=utf-8

import copy


class Solution:
    def permute(self, nums):
        def backtracking(nums, index, tmp, idx_tmp):
            if len(nums) == len(tmp):
                if tmp not in results:
                    results.append(tmp[:])
            else:
                for idx, n in enumerate(nums):
                    if idx in idx_tmp:
                        continue
                    tmp.append(n)
                    idx_tmp.append(idx)
                    backtracking(nums, idx, tmp, idx_tmp)
                    tmp.pop()
                    idx_tmp.pop()

        results = []
        tmp = []
        idx_tmp = []
        backtracking(nums, 0, tmp, idx_tmp)
        return results
