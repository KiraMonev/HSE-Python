"""
leetcode.com/problem-list/binary-tree
url: https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, float("-INF"))

    def dfs(self, root, m):
        if root is None:
            return 0

        m = max(m, root.val)
        count = self.dfs(root.left, m) + self.dfs(root.right, m)
        if root.val >= m:
            count += 1

        return count
