# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        # def dfs(parent, child, f):
        #     if not child:
        #         return
        #
        #     dfs(child, child.left, 'left')
        #     dfs(child, child.right, 'right')
        #     p = child
        #     if p.left is None and p.right is None and p.val == 0:
        #         if f == 'left':
        #             parent.left = None
        #         else:
        #             parent.right = None
        #
        # if root and root.left:
        #     dfs(root, root.left, 'left')
        # if root and root.right:
        #     dfs(root, root.right, 'right')
        # return root
        def containsOne(node):
            if not node: return False
            a1 = containsOne(node.left)
            a2 = containsOne(node.right)
            if not a1: node.left = None
            if not a2: node.right = None
            return node.val == 1 or a1 or a2

        return root if containsOne(root) else None

