# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []

        def dfs(root):
            if not root:
                return

            dfs(root.left)
            dfs(root.right)
            ans.append(root.val)

        dfs(root)
        return ans
