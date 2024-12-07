"""
leetcode.com/problem-list/binary-tree
url: https://leetcode.com/problems/validate-binary-search-tree/description/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.bst(root)

    def bst(self, root, min_val=-(2**31) - 1, max_val=2**31 + 1):
        if root is None:
            return True

        if not (min_val < root.val < max_val):
            return False

        return self.bst(root.left, min_val, root.val) and self.bst(
            root.right, root.val, max_val
        )
