from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        s = 0
        for v in A:
            if v % 2 == 0:
                s += v
        for i in range(len(A)):
            val = queries[i][0]
            idx = queries[i][1]
            if A[idx] % 2 == 0 and (A[idx] + val) % 2 != 0:
                s -= A[idx]
            elif A[idx] % 2 != 0 and (A[idx] + val) % 2 == 0:
                s += A[idx] + val
            elif A[idx] % 2 == 0 and (A[idx] + val) % 2 == 0:
                s += val
            res.append(s)
            A[idx] += val
        return res
