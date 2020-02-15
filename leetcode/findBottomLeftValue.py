# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        from collections import deque
        q = deque()
        q.appendleft((root, 1))
        left = root.val
        max_depth = 0
        while q:
            t, dep = q.pop()
            if max_depth < dep:
                left = t.val
                max_depth = dep
            if t.left:
                q.appendleft((t.left, dep + 1))
            if t.right:
                q.appendleft((t.right, dep + 1))
        return left
