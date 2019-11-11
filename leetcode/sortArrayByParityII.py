from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A) - 1
        while left < right:
            while left % 2 !=  A[left] % 2 and left < len(A):
                left += 1
            while right % 2 != A[right] % 2 and right >= 0:
                right -= 1

            if left < right:
                A[left], A[right] = A[right], A[left]
        return A
