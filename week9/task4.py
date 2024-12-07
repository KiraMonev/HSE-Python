"""
leetcode.com/problem-list/binary-tree
url: https://leetcode.com/problems/delete-node-in-a-bst/description/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.remove(root, key)

    def findmin(self, root):
        if root is None:
            return None
        if root.left is None:
            return root
        return self.findmin(root.left)

    def remove(self, root, key):
        if root is None:
            return

        if key > root.val:
            root.right = self.remove(root.right, key)
        elif key < root.val:
            root.left = self.remove(root.left, key)
        elif key == root.val:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                minval = self.findmin(root.right)
                root.val = minval.val
                root.right = self.remove(root.right, minval.val)
        return root
