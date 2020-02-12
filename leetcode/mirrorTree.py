# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return
            tmp = root.left
            root.left = root.right
            root.right = tmp
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return root
