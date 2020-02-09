# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        ans = []
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            ans.append(root.val)
            dfs(root.right)
        dfs(root)
        return ans[k - 1]
