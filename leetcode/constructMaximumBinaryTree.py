# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.construct(nums, 0, len(nums))

    def construct(self, nums, i, j):
        if i == j:
            return
        val = max(nums[i: j])
        idx = nums.index(val)
        root = TreeNode(val)
        root.left = self.construct(nums, i, idx)
        root.right = self.construct(nums, idx + 1, j)
        return root

