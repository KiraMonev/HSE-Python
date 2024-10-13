"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/insert-delete-getrandom-o1/description/
"""

import random


class RandomizedSet:

    def __init__(self):
        self.arr = []

    def insert(self, val: int) -> bool:
        if val in self.arr:
            return False
        else:
            self.arr.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.arr:
            self.arr.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.arr)
