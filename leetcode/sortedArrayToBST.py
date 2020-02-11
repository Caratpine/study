# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.construct(nums, 0, len(nums))

    def construct(self, nums, i, j):
        if not nums[i: j]:
            return
        idx = (j + i) // 2
        root = TreeNode(nums[idx])
        root.left = self.construct(nums, i, idx)
        root.right = self.construct(nums, idx + 1, j)
        return root
