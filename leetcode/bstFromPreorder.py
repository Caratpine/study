# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder[0])
        for val in preorder[1:]:
            p = root
            while p:
                if val < p.val:
                    if p.left:
                        p = p.left
                    else:
                        p.left = TreeNode(val)
                        break
                elif val > p.val:
                    if p.right:
                        p = p.right
                    else:
                        p.right = TreeNode(val)
                        break
        return root
