"""
leetcode.com/problem-list/sliding-window
url: https://leetcode.com/problems/permutation-in-string/description/
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dicts1 = {}
        for i in s1:
            if i in dicts1:
                dicts1[i] += 1
            else:
                dicts1[i] = 1

        n, s = len(s1), 0
        t = {}
        temp = []

        for j in s2:
            if j in dicts1:
                if j in t:
                    t[j] += 1
                else:
                    t[j] = 1
                temp.append(j)
                s += 1

                if s > n:
                    a = temp.pop(0)
                    if t[a] == 1:
                        del t[a]
                    else:
                        t[a] -= 1
                    s -= 1

                if s == n and t == dicts1:
                    return True
            else:
                t.clear()
                temp.clear()
                s = 0

        return False
