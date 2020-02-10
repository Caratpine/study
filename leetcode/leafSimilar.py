# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        ans1 = []
        ans2 = []

        def dfs(root, ans):
            if not root:
                return
            if root.left is None and root.right is None:
                ans.append(root.val)
            dfs(root.left, ans)
            dfs(root.right, ans)

        dfs(root1, ans1)
        dfs(root2, ans2)
        return ans1 == ans2

