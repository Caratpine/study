class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for v in s:
            if v in d.keys():
                d[v] += 1
            else:
                d[v] = 1

        sum = 0
        for k, v in d.items():
            sum += v // 2 * 2
            if sum % 2 == 0 and v % 2 == 1:
                sum += 1
        return sum

