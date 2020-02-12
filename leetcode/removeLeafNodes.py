# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        def dfs(root):
            if not root:
                return
            root.left = dfs(root.left)
            root.right = dfs(root.right)
            if not root.left and not root.right:
                if root.val == target:
                    return
            return root
        r = dfs(root)
        return r
