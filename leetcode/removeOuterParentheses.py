class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        l = 0
        res = ''
        for c in S:
            if c == '(':
                l += 1
                if l > 1:
                    res += c
            else:
                if l > 1:
                    res += c
                l -= 1
        return res
