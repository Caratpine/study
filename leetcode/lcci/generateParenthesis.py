class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtracing(s, n, left=0, right=0):
            if len(s) == 2 * n:
                ans.append(s)
                return
            else:
                if left < n:
                    backtracing(s + '(', n, left + 1, right)
                if right < left:
                    backtracing(s + ')', n, left, right + 1)
        backtracing('', n)
        return ans
