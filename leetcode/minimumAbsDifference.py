from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        res = {}
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i-1])
            if diff in res.keys():
                res[diff].append([arr[i-1], arr[i]])
            else:
                res[diff] = [[arr[i-1], arr[i]]]

        key = min(res.keys())
        return res[key]
