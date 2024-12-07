"""
leetcode.com/problem-list/binary-tree
url: https://leetcode.com/problems/find-duplicate-subtrees/description/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> list[TreeNode]:
        self.freq = {}
        self.res = []

        self.traverse(root)
        return self.res

    def traverse(self, node):
        if not node:
            return ""
        left = self.traverse(node.left)
        right = self.traverse(node.right)
        subtree = left + "," + right + "," + str(node.val)
        self.freq[subtree] = self.freq.get(subtree, 0) + 1
        if self.freq[subtree] == 2:
            self.res.append(node)
        return subtree
