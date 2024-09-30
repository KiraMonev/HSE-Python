"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/maximum-product-of-word-lengths/description/
"""


class Solution:
    def maxProduct(self, words: list[str]) -> int:
        ans = 0
        for i in range(len(words)):
            first_word = words[i]
            first_word_letters = set(words[i])
            for j in range(i + 1, len(words)):
                second_word = words[j]
                second_word_letters = set(words[j])
                if any(letter in first_word_letters for letter in second_word_letters):
                    continue

                ans = max(len(first_word) * len(second_word), ans)

        return ans
