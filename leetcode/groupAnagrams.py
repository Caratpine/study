# coding=utf-8

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in d.keys():
                d[key].append(s)
            else:
                d[key] = []
                d[key].append(s)

        return d.values()
