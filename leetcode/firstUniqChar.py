# coding=utf-8


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for c in s:
            if c in d.keys():
                d[c] += 1
            else:
                d[c] = 1

        for idx, c in enumerate(s):
            if d[c] == 1:
                return idx
        return -1
