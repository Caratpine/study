# coding=utf-8

from typing import List


class Solution:
    def countBits(self, num: int) -> List[int]:
        result = []
        for i in range(num + 1):
            if i == 0:
                result.append(0)
            elif i % 2 == 1:
                result.append(result[i - 1] + 1)
            elif i % 2 == 0:
                result.append(result[int(i / 2)])
        return result
