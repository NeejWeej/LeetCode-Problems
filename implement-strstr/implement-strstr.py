class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        idx = 0
        if needle == '':
            return 0
        batch = len(needle)
        end_hay = len(haystack)
        for idx, val in enumerate(haystack):
            if val == needle[0]:
                possib_match = haystack[idx: min(end_hay, idx + batch)]
                if needle == possib_match:
                    return idx
        return -1