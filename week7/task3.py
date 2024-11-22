"""
leetcode.com/problem-list/sliding-window
url:
"""


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        res, cur, l, cur_sub = 0, 0, 0, 0
        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                cur += 1
                cur_sub = 0

            while cur == k:
                if nums[l] % 2 == 1:
                    cur -= 1
                l += 1
                cur_sub += 1
            res += cur_sub

        return res
