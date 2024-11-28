"""
leetcode.com/problem-list/sliding-window
url: https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/
"""


class Solution:
    def resultsArray(self, nums: list[int], k: int) -> list[int]:
        size = len(nums)
        res = []
        if k == 1:
            return nums
        for _ in range(size - k + 1):
            i = _
            j = _
            count = 0
            while i < j + k - 1:
                if nums[i] != nums[i + 1] - 1 or nums[i] >= nums[i + 1]:
                    res.append(-1)
                    i += 1
                    break
                else:
                    count += 1
                i += 1

                if count == k - 1:
                    res.append(nums[i])
                    break

        return res
