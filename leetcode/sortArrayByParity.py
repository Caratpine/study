from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        left = 0
        right = len(A) - 1
        while left < right:
            while True:
                if A[left] % 2 != 0 or left == len(A) - 1:
                    break
                left += 1
            while True:
                if A[right] % 2 != 1 or right == 0:
                    break
                right -= 1
            if left < right:
                tmp = A[left]
                A[left] = A[right]
                A[right] = tmp
                left += 1
                right -= 1
        return A
