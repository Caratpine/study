# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.is_mirror(root, root)

    def is_mirror(self, t1: TreeNode, t2: TreeNode) -> bool:
        if t1 is None and t2 is None:
            return True

        if t1 is None or t2 is None:
            return False

        return (t1.val == t2.val) and self.is_mirror(t1.right, t2.left) and self.is_mirror(t1.left, t2.right)
