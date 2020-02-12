# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> List[int]:
        ans = []

        def dfs(root):
            if not root:
                return

            for n in root.children:
                dfs(n)
            ans.append(root.val)

        dfs(root)
        return ans
