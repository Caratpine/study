class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans = 0

        def dfs(grandparent, parent, node):
            if not node:
                return
            if grandparent.val % 2 == 0:
                nonlocal ans
                ans += node.val
            dfs(parent, node, node.left)
            dfs(parent, node, node.right)

        if root.left:
            dfs(root, root.left, root.left.left)
            dfs(root, root.left, root.left.right)
        if root.right:
            dfs(root, root.right, root.right.left)
            dfs(root, root.right, root.right.right)

        return ans

