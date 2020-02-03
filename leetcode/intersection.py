from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            return self.helper(nums1, nums2)
        else:
            return self.helper(nums2, nums1)

    def helper(self, nums1, nums2):
        return list(set([x for x in nums1 if x in nums2]))
