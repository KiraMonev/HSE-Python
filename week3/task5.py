"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/making-file-names-unique/description/
"""


class Solution:
    def getFolderNames(self, names: list[str]) -> list[str]:
        name_min = dict()
        ans = []
        for name in names:
            if name not in name_min:
                ans.append(name)
                name_min[name] = 0
            else:
                k = name_min[name] + 1
                tmp = f"{name}({str(k)})"
                while tmp in name_min:
                    k += 1
                    tmp = f"{name}({str(k)})"
                ans.append(tmp)
                name_min[name] = k
                name_min[tmp] = 0

        return ans
