from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            return self.helper(nums1, nums2)
        else:
            return self.helper(nums2, nums1)

    def helper(self, nums1, nums2):
        d = {}
        res = []
        for n in nums1:
            if n in d.keys():
                d[n] += 1
            else:
                d[n] = 1

        for n in nums2:
            if n in d.keys() and d[n] > 0:
                res.append(n)
                d[n] -= 1
        return res
