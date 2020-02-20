from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        import copy

        def backtracing(s, i, k):
            if i == len(s):
                ans.append(copy.copy(k))
                return
            for idx in range(i, len(s)):

                if self.isPalindrome(s[i:idx + 1]):
                    k.append(s[i:idx + 1])
                    backtracing(s, idx + 1, k)
                    k.pop()

        backtracing(s, 0, [])
        return ans

    def isPalindrome(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
