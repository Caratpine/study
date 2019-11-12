from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        rs = []
        for n in A:
            rs.append(n * n)
        return sorted(rs)
