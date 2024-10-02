"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/design-browser-history/description/
"""


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history_list = [homepage]
        self.cur_pos = 0
        self.size = 1

    def visit(self, url: str) -> None:
        if self.cur_pos + 1 >= len(self.history_list):
            self.history_list.append(url)
        else:
            self.history_list[self.cur_pos + 1] = url
        self.cur_pos += 1
        self.size = self.cur_pos + 1

    def back(self, steps: int) -> str:
        self.cur_pos = max(0, self.cur_pos - steps)
        return self.history_list[self.cur_pos]

    def forward(self, steps: int) -> str:
        self.cur_pos = min(self.size - 1, self.cur_pos + steps)
        return self.history_list[self.cur_pos]
