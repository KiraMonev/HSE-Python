class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letter_from_num = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = []

        def comb(combination, next_digits):
            if not next_digits:
                res.append(combination)
                return

            for letter in letter_from_num[next_digits[0]]:
                comb(combination + letter, next_digits[1:])

        comb("", digits)
        return res
