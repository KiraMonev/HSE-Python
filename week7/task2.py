"""
leetcode.com/problem-list/sliding-window
url: https://leetcode.com/problems/arithmetic-slices/description/
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        k = 0
        for i in range(len(nums) - 2):
            temp = nums[i : 3 + i]
            a = temp[1] - temp[0]
            b = temp[2] - temp[1]
            if a == b:
                k += 1
                for j in range(i + 3, len(nums)):
                    temp.append(nums[j])
                    if a == (temp[-1] - temp[-2]):
                        k += 1
                    else:
                        break
        return k
