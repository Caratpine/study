# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ans = []
        def dfs(root):
            if not root:
                return True
            l = dfs(root.left)
            if ans and ans[-1] >= root.val:
                return False
            ans.append(root.val)
            r = dfs(root.right)
            return l and r
        return dfs(root)
