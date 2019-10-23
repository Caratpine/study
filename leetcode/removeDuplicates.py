class Solution:
    def removeDuplicates(self, S: str) -> str:
        s = []
        for v in S:
            if len(s) == 0:
                s.append(v)
            else:
                if s[-1] == v:
                    s.pop()
                else:
                    s.append(v)
        return ''.join(s)
