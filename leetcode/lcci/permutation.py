class Solution:
    def permutation(self, S: str) -> List[str]:
        ans = []

        def backtracing(s, tmp):
            if len(tmp) == len(s):
                ans.append(''.join(tmp))
            for c in s:
                if c in tmp:
                    continue
                tmp.append(c)
                backtracing(s, tmp)
                tmp.pop()

        backtracing(S, [])
        return ans
