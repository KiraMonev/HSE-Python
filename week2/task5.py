"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/adding-spaces-to-a-string/description/
"""


class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        s_arr = list(s)

        for idx in spaces:
            t = " " + s[idx]
            s_arr[idx] = t

        ans = "".join(s_arr)

        return ans
