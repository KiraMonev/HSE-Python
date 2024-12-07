"""
leetcode.com/problem-list/binary-tree
url: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.cur = None
        self.dfs(root)

    def dfs(self, node):
        if not node:
            return
        left, right = node.left, node.right
        node.left = None
        if self.cur:
            self.cur.right = node
            self.cur = self.cur.right
        else:
            self.cur = node
        self.dfs(left)
        self.dfs(right)
