"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/reverse-words-in-a-string/?envType=problem-list-v2&envId=string
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        s_dirt_list = s.split(" ")
        res_list = []
        for word in s_dirt_list:
            if word != "":
                res_list.append(word)
        res = " ".join(res_list[len(res_list) - 1 :: -1])

        return res
