"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/permutations/description/
"""


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = []
        temp = []
        self.backtrack(ans, temp, nums)
        return ans

    def backtrack(self, ans, temp, nums):
        if len(temp) == len(nums):
            ans.append(temp[:])
        else:
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                temp.append(nums[i])
                self.backtrack(ans, temp, nums)
                temp.pop()
