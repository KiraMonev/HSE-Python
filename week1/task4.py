"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/minimum-window-substring/description/
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        target = {}
        for char in t:
            target[char] = target.get(char, 0) + 1

        req = len(target)

        l, r = 0, 0
        formed = 0
        window = {}

        ans = float("inf"), None, None

        while r < len(s):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in target and window[char] == target[char]:
                formed += 1

            while l <= r and formed == req:
                char = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window[char] -= 1
                if char in target and window[char] < target[char]:
                    formed -= 1

                l += 1
            r += 1

        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
