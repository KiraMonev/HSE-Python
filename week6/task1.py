"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/minimum-size-subarray-sum/description/
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = 1000000
        left = 0
        cur_sum = 0

        for r in range(len(nums)):
            cur_sum += nums[r]

            while cur_sum >= target:
                if r - left + 1 < min_len:
                    min_len = r - left + 1
                cur_sum -= nums[left]
                left += 1

        return min_len if min_len != 1000000 else 0
