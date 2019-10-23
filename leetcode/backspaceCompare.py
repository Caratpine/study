class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s1 = []
        s2 = []
        for v in S:
            if v == '#':
                if len(s1) != 0:
                    s1.pop()
            else:
                s1.append(v)

        for v in T:
            if v == '#':
                if len(s2) != 0:
                    s2.pop()
            else:
                s2.append(v)

        if len(s1) == len(s2):
            while len(s1) != 0 and len(s2) != 0:
                if s1.pop() != s2.pop():
                    return False
            return True
        else:
            return False
