"""
leetcode.com/problem-list/sliding-window
url: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
"""


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        t = 0

        for i in range(k):
            if s[i] in vowels:
                t += 1

        vow_num = t

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                t -= 1

            if s[i] in vowels:
                t += 1

            vow_num = max(vow_num, t)

        return vow_num
