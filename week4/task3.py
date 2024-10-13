"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/median-of-two-sorted-arrays/description/
"""


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums = sorted(nums)
        mid = (
            float(nums[len(nums) // 2])
            if len(nums) % 2 == 1
            else (float(nums[len(nums) // 2 - 1]) + float(nums[(len(nums) // 2)])) / 2
        )
        return mid
