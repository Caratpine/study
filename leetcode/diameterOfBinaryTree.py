# coding=utf-8


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.sum = 0

        def helper(root: TreeNode):
            if root is None:
                return 0
            l = helper(root.left)
            r = helper(root.right)
            self.sum = max(r + l, self.sum)
            return max(l, r) + 1

        helper(root)
        return self.sum
