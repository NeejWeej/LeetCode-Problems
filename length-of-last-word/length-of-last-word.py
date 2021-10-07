class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = len(s) - 1
        while s[idx] == ' ':
            idx -= 1
        start = idx
        while 0 <= idx and s[idx] != ' ':
            idx -= 1
        end = idx
        return start - end