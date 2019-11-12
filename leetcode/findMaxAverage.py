from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k > len(nums):
            return 0
        s = 0
        for i in range(0, k):
            print(i)
            s += nums[i]
        m = s
        for i in range(k, len(nums)):
            print(i)
            s = s + nums[i] - nums[i - k]
            m = max(m, s)
        return m / k
