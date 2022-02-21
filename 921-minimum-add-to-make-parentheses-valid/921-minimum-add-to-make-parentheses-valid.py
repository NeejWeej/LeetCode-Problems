class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        offset = 0
        ans = 0
        for char in s:
            if char == '(':
                offset += 1
            elif char == ')':
                offset -= 1
            if offset == -1:
                ans += 1
                offset = 0
        return ans + offset