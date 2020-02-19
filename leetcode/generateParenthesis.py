# coding=utf-8

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(A = []):
            print(A)
            if len(A) == 2*n:
                print('_' * 10)
                if valid(A):
                    ans.append("".join(A))
            else:
                A.append('(')
                generate(A)
                A.pop()
                A.append(')')
                generate(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0

        ans = []
        generate()
        return ans

    def generateParenthesis1(self, n: int) -> List[str]:
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


if __name__ == '__main__':
    Solution().generateParenthesis(2)
