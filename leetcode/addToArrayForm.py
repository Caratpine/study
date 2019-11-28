from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A[-1] += K
        c = 0
        for i in range(len(A) -1, -1, -1):
            c, A[i] = divmod(A[i], 10)
            if i:
                A[i-1] += c
        if c:
            A = list(map(int, str(c))) + A
        return A

