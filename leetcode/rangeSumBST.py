# coding=utf-8


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        result = []

        def helper(root: TreeNode):
            if root is None:
                return
            if root.val >= L and root.val <= R:
                result.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        return sum(result)
