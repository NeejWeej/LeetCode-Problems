class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_chars = {}
        best = cur = 0
        start = 0
        for idx, c in enumerate(s):
            if c not in seen_chars:
                seen_chars[c] = idx
                cur += 1
                best = max(best, cur)
            else:
                new_start = seen_chars.get(c) + 1
                for i in range(start, new_start):
                    seen_chars.pop(s[i])
                start = new_start
                seen_chars[c] = idx
                cur = idx - start + 1
        return best