from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        d = dict(Counter(s))
        l = ['' for i in range(len(s) + 1)]
        for k, v in d.items():
            l[v] += k * v

        res = []

        for i in range(-1, -len(l) - 1, -1):
            if l[i] != '':
                res.append(l[i])
        return ''.join(res)
