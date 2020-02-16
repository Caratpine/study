class Solution:
    def isUnique(self, astr: str) -> bool:
        if len(astr) <= 1:
            return True
        astr = sorted(astr)
        for i in range(len(astr) - 1):
            if astr[i] == astr[i + 1]:
                return False
        return True
