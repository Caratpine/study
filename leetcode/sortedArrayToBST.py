# Definition for a binary tree node.
from typing import List, Union,


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

    def sortedArrayToBST2(self, nums: List[int]) -> Union[TreeNode, None]:
        if len(nums) == 0:
            return None

        idx = len(nums) // 2
        root = TreeNode(nums[idx])
        root.left = self.sortedArrayToBST2(nums[0:idx])
        root.right = self.sortedArrayToBST2(nums[idx + 1:len(nums)])
        return root
