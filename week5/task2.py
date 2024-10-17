"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/sort-characters-by-frequency/description/
"""


class Solution:
    def frequencySort(self, s: str) -> str:
        s_dict = {}
        for i in range(len(s)):
            if s[i] not in s_dict.keys():
                s_dict[s[i]] = s.count(s[i])

        ans = sorted(s_dict.items(), key=lambda x: x[1], reverse=True)
        ans_s = ""
        for i in range(len(s_dict.keys())):
            letter = ans[i][0]
            letter_count = ans[i][1]
            for j in range(letter_count):
                ans_s += letter

        return ans_s
