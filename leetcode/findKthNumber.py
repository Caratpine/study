# coding=utf-8

from typing import List


class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        l = self.lexicalOrder(n)
        return l[k-1]

    def lexicalOrder(self, n: int) -> List[int]:
        l = []
        for i in range(1, 10):
            if i <= n:
                l.append(i)
                self.add(l, n, i)
            else:
                break
        return l

    def add(self, l, n, start_num):
        start_num *= 10
        for i in range(1, 10):
            if start_num <= n:
                l.append(start_num)
                self.add(l, n, start_num)
                start_num += 1
            else:
                return
