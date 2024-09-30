"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-case-permutation/description/
"""


class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        ans = []

        self.solve(ans, s, "")
        return ans

    def solve(self, ans, ip, op):
        if ip == "":
            ans.append(op)
            return

        if ip[0].isalpha():
            op1 = op + ip[0].lower()
            op2 = op + ip[0].upper()
            self.solve(ans, ip[1:], op1)
            self.solve(ans, ip[1:], op2)
        else:
            self.solve(ans, ip[1:], op + ip[0])
