# coding=utf-8


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            factorial[i] = factorial[i - 1] * i
        used = [False for _ in range(n + 1)]
        path = []

        def dfs(used, n, index, path, k):
            if index == n:
                return
            c = factorial[n - index - 1]
            for i in range(1, n + 1):
                if used[i]:
                    continue
                if c < k:
                    k -= c
                    continue
                path.append(i)
                used[i] = True
                dfs(used, n, index + 1, path, k)

        dfs(used, n, 0, path, k)
        return ''.join([str(i) for i in path])
