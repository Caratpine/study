# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        ans = []

        def dfs(root, s):
            if not root:
                return
            s += str(root.val)
            if root.left is None and root.right is None:
                ans.append(s)
            s += '->'
            dfs(root.left, s)
            dfs(root.right, s)
        dfs(root, '')
        return ans
