# coding=utf-8


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = list(range(1, n + 1))
        results = []

        def backtracking(tmp):
            if len(nums) == len(tmp):
                results.append(tmp[:])
            else:
                for n in nums:
                    if n in tmp:
                        continue
                    tmp.append(n)
                    backtracking(tmp)
                    tmp.pop()
        backtracking([])
        return ''.join(map(str, results[k - 1]))
