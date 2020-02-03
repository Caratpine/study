class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.isIsomorphicHelper(s, t) and self.isIsomorphicHelper(t, s)

    def isIsomorphicHelper(self, s: str, t: str) -> bool:
        d = {}
        for idx, v in enumerate(s):
            if v in d.keys():
                if t[idx] != d[v]:
                    return False
            else:
                d[v] = t[idx]
        return True
