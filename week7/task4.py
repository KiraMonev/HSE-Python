"""
leetcode.com/problem-list/sliding-window
url: https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/description/
"""


class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = "aeiou"
        ans = 0
        cnt = prev = -1
        for i, x in enumerate(word):
            cur = vowels.index(x)
            if cnt >= 0:
                if 0 <= cur - prev <= 1:
                    cnt += 1
                    if x == "u":
                        ans = max(ans, cnt)
                elif x == "a":
                    cnt = 1
                else:
                    cnt = -1
            elif x == "a":
                cnt = 1
            prev = cur
        return ans
