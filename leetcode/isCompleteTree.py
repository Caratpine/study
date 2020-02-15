# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        from collections import deque
        q = deque()
        q.appendleft(root)

        ans = []
        while q:
            t = q.pop()
            ans.append(t.val if t else None)
            if t:
                q.appendleft(t.left)
                q.appendleft(t.right)
        while not ans[-1]:
            ans.pop()
        return False if None in ans else True
