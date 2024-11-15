"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n, k = len(s), len(p)
        if k > n:
            return []

        p_dict = self.build_dict(p)
        win_dict = self.build_dict(s[: k - 1])

        ans = []
        for i in range(k - 1, n):
            win_dict[s[i]] = win_dict.get(s[i], 0) + 1

            if win_dict == p_dict:
                ans.append(i - k + 1)

            start_char = s[i - k + 1]
            win_dict[start_char] -= 1
            if win_dict[start_char] == 0:
                del win_dict[start_char]

        return ans

    def build_dict(self, string):
        char_count = {}
        for char in string:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count
