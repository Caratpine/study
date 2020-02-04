class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = {}
        for v in t:
            if v in d.keys():
                d[v] += 1
            else:
                d[v] = 1

        for v in s:
            if v in  and d[v] > 0:
                d[v] -= 1

        for k, v in d.items():
            if v == 1:
                return k

