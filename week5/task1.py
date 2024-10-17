"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/majority-element-ii/description/
"""


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        rule = len(nums) // 3
        nums_dict = {}

        for i in range(len(nums)):
            if nums[i] not in nums_dict.keys():
                nums_dict[nums[i]] = nums.count(nums[i])

        ans = []
        for key, val in nums_dict.items():
            if val > rule:
                ans.append(key)

        return ans
