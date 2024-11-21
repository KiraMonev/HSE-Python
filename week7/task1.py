"""
leetcode.com/problem-list/sliding-window
url: https://leetcode.com/problems/repeated-dna-sequences/description/
"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        ans_dict = dict()
        ans_arr = []

        for i in range(len(s) - 9):
            DNA = s[i : i + 10]
            if DNA in ans_dict:
                ans_dict[DNA] += 1
            else:
                ans_dict[DNA] = 1

        for key, val in ans_dict.items():
            if val > 1:
                ans_arr.append(key)

        return ans_arr
