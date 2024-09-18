class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = s
        longest_sub_str = ""
        sub_str = ""
        for i in range(0, len(word)):
            sub_str = ""
            for j in range(i, len(word)):
                if word[j] not in sub_str:
                    sub_str += word[j]
                else:
                    if len(sub_str) > len(longest_sub_str):
                        longest_sub_str = sub_str
                    break

                if j == (len(word) - 1):
                    if len(sub_str) > len(longest_sub_str):
                        longest_sub_str = sub_str
                    break

        return len(longest_sub_str)
