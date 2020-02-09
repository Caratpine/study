# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            root = TreeNode(val)
            return root
        node = root
        while node:
            if val > node.val:
                if node.right is None:
                    node.right = TreeNode(val)
                    return root
                node = node.right
            else:
                if node.left is None:
                    node.left = TreeNode(val)
                    return root
                node = node.left
