# coding=utf-8


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        result = []

        def helper(root: TreeNode, val: int):
            if root is None:
                return

            if root.val == val:
                result.append(root)

            helper(root.left, val)
            helper(root.right, val)

        helper(root, val)
        return result[0] if result else None
