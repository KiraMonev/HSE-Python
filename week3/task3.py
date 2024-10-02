"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/design-a-stack-with-increment-operation/description/
"""


class CustomStack:
    def __init__(self, maxSize: int):
        self.arr = []
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.arr) <= self.size - 1:
            self.arr.append(x)

    def pop(self) -> int:
        if len(self.arr) > 0:
            last_num = self.arr[-1]
            self.arr.pop()
            return last_num
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        if k > self.size:
            k = self.size
        if k > len(self.arr):
            k = len(self.arr)

        if len(self.arr) != 0:
            for i in range(0, k):
                self.arr[i] += val
