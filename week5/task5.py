"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/html-entity-parser/description/
"""


class Solution:
    def entityParser(self, text: str) -> str:
        text = text.replace("&quot;", '"').replace("&apos;", "'")
        text = text.replace("&gt;", ">").replace("&lt;", "<")
        text = text.replace("&frasl;", "/").replace("&amp;", "&")

        return text
