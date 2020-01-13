# coding=utf-8

from typing import List


class Solution(object):
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        l = sorted(intervals)
        r = []
        n = 0
        for idx, v in enumerate(l[1:], start=1):
            if len(r) == 0:
                l1 = l[idx][1] - l[idx][0]
                l0 = l[idx-1][1] - l[idx-1][0]
                if l0 <= l1:
                    r.append(l[idx-1])
                    if l[idx - 1][0] < l[idx][0] < l[idx - 1][1] or l[idx - 1][0] < l[idx][1] < l[idx - 1][1]:
                        n += 1
                else:
                    r.append(l[idx])
                    if l[idx][0] < l[idx-1][0] < l[idx][1] or l[idx][0] < l[idx-1][1] < l[idx][1]:



