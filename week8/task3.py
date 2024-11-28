"""
leetcode.com/problem-list/sliding-window
url: https://leetcode.com/problems/count-complete-subarrays-in-an-array/description/
"""


class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        count = 0
        n = len(nums)
        dis_k = len(set(nums))

        left = 0
        window = {}

        for right in range(n):
            window[nums[right]] = window.get(nums[right], 0) + 1

            while len(window) == dis_k:
                count += n - right
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                left += 1

        return count
