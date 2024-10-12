"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/sort-colors/description/
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        for i in range(len(nums) - 1):
            for j in range(len(nums) - 1):
                if nums[j] > nums[j + 1]:
                    t = nums[j + 1]
                    nums[j + 1] = nums[j]
                    nums[j] = t
