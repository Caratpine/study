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
                return
            if root.left:
                self.sum += 1
                print(self.sum)
            elif root.right:
                self.sum += 1

            helper(root.left)
            helper(root.right)
        helper(root)
        return self.sum
