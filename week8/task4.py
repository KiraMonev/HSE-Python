"""
leetcode.com/problem-list/sliding-window
url: https://leetcode.com/problems/find-the-longest-equal-subarray/description/
"""


class Solution:
    def longestEqualSubarray(self, nums: list[int], k: int) -> int:
        freq = {}
        left = 0
        maxf = 0
        for right in range(len(nums)):
            if nums[right] not in freq:
                freq[nums[right]] = 0
            freq[nums[right]] += 1

            while (right - left + 1) - k > freq[nums[left]]:
                freq[nums[left]] -= 1
                left += 1

            maxf = max(maxf, freq[nums[right]])

        return maxf
