# coding=utf-8


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_dep = 0

    def maxDepth(self, root) -> int:
        if not root:
            return 0
        stack = [(root, 0)]
        depth = 0
        while stack:
            node, curr_depth = stack.pop()
            if node is not None:
                depth = max(depth, curr_depth)
            stack.append((node.left, curr_depth + 1))
            stack.append((node.right, curr_depth + 1))
        return depth

    def maxDepth2(self, root: TreeNode) -> int:
        def dfs(root, dep):
            if not root:
                return
            if dep > self.max_dep:
                self.max_dep = dep
            dfs(root.left, dep + 1)
            dfs(root.right, dep + 1)
        dfs(root, 1)
        return self.max_dep
