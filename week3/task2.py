"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/four-divisors/description/
"""


class Solution:
    def sumFourDivisors(self, nums: list[int]) -> int:
        ans_num_list = {}
        ans_sum = 0
        for num in nums:
            num_divisors = self.getDivisors(num)
            if len(num_divisors) == 4:
                if num in ans_num_list.keys():
                    ans_sum += sum(num_divisors)
                else:
                    ans_num_list[num] = num_divisors
                    ans_sum += sum(num_divisors)

        return ans_sum

    def getDivisors(self, num):
        divisors = set()
        for i in range(1, int((num**0.5) + 1)):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num // i)

        return divisors
