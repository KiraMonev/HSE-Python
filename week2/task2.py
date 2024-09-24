"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/bulls-and-cows/description/
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_count = {}
        guess_count = {}

        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_count[s] = secret_count.get(s, 0) + 1
                guess_count[g] = guess_count.get(g, 0) + 1

        for g in guess_count:
            if g in secret_count:
                cows += min(secret_count[g], guess_count[g])

        ans = f"{bulls}A{cows}B"
        return ans
