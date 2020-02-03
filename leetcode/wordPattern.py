class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        d = {}
        l = str.split(' ')
        if len(pattern) != len(l):
            return False
        for idx, v in enumerate(pattern):
            if v in d.keys():
                if l[idx] != d[v]:
                    return False
            else:
                if l[idx] in d.values():
                    return False
                d[v] = l[idx]
        return True
