"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if not nums:
            return [-1, -1]

        first_idx = self.find_first_idx(nums, target)

        if first_idx == -1:
            return [-1, -1]

        last_idx = self.find_last_idx(nums, target)

        return [first_idx, last_idx]

    def find_first_idx(self, nums, target):
        left, right = 0, len(nums) - 1
        first_pos = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first_pos = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return first_pos

    def find_last_idx(self, nums, target):
        left, right = 0, len(nums) - 1
        last_pos = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last_pos = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return last_pos
