class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for v in s:
            if not stack or stack[-1][0] != v:
                stack.append([v, 1])
            elif stack[-1][1] + 1 < k:
                stack[-1][1] += 1
            else:
                stack.pop()
        res = []
        for s, n in stack:
            res.append(s * n)
        return ''.join(res)

