"""
leetcode.com/problem-list/binary-tree
url: https://leetcode.com/problems/validate-binary-tree-nodes/description/
"""


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: list[int], rightChild: list[int]
    ) -> bool:
        checked = set([i for i in range(n)])

        for i in range(n):
            if leftChild[i] in checked:
                checked.remove(leftChild[i])
            if rightChild[i] in checked:
                checked.remove(rightChild[i])

        if len(checked) != 1:
            return False

        check = [False for _ in range(n)]
        checked = list(checked)

        while checked:
            nw = []
            for num in checked:
                if num == -1:
                    continue
                if check[num]:
                    return False
                check[num] = True
                nw.append(leftChild[num])
                nw.append(rightChild[num])
            checked = nw
        return sum(check) == n
