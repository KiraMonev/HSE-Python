"""
leetcode.com/problem-list/binary-tree
url: https://leetcode.com/problems/even-odd-tree/description/
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        layer = [root]
        level = 0
        while layer:
            nextlayer = []
            if level % 2 == 0:
                lastval = 0
            else:
                lastval = 1000001

            for node in layer:
                if level % 2 == 0:
                    if node.val % 2 == 0 or node.val <= lastval:
                        return False
                else:
                    if node.val % 2 != 0 or node.val >= lastval:
                        return False

                lastval = node.val

                if node.left:
                    nextlayer.append(node.left)
                if node.right:
                    nextlayer.append(node.right)

            layer = nextlayer
            level += 1

        return True
