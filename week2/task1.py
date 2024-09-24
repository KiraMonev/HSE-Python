"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/simplify-path/description/
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path
        s_arr = s.split("/")
        stack = []
        for word in s_arr:
            if word == "" or word == ".":
                continue
            if word == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(word)

        ans = "/" + "/".join(stack)

        return ans
