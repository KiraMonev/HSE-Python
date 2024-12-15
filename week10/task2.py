"""
leetcode.com/problem-list/binary-tree
url: https://leetcode.com/problems/delete-nodes-and-return-forest/description/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(
        self, root: Optional[TreeNode], to_delete: list[int]
    ) -> list[TreeNode]:

        to_delete = set(to_delete)
        res = []

        self.traverse(root, None, to_delete, res)
        return res

    def traverse(self, node, parent, to_delete, res):
        if not node:
            return None
        r = node

        if node.val in to_delete:
            r = None

        if parent is None:

            if r is not None:
                res.append(r)

        node.left = self.traverse(node.left, r, to_delete, res)
        node.right = self.traverse(node.right, r, to_delete, res)

        return r
