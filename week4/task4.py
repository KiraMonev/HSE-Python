"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/merge-intervals/description/
"""


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        ans = []
        intervals.sort(key=lambda x: x[0])

        prev = intervals[0]

        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                ans.append(prev)
                prev = interval

        ans.append(prev)

        return ans
