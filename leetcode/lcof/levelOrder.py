# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        ans = []
        if not root:
            return ans
        from collections import deque
        q = deque()
        q.appendleft(root)
        while q:
            r = q.pop()
            ans.append(r.val)
            if r.left:
                q.appendleft(r.left)
            if r.right:
                q.appendleft(r.right)
        return ans
