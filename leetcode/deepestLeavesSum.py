# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max = -1
        self.total = 0

    def deepestLeavesSum(self, root: TreeNode) -> int:
        def dfs(root, dep):
            if not root:
                return
            if dep > self.max:
                self.max, self.total = dep, root.val
            elif dep == self.max:
                self.total += root.val
            dfs(root.left, dep + 1)
            dfs(root.right, dep + 1)

        dfs(root, 0)
        return self.total

