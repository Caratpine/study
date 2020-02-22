class Solution:
    def climbStairs(self, n: int) -> int:
        d = {}
        def f(n):
            if n == 1 or n == 2:
                return n
            else:
                if n in d.keys():
                    return d[n]
                else:
                    s = f(n - 1) + f(n - 2)
                    d[n] = s
                    return s
        return f(n)
