class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        best = 1
        seen = {s[0]: 1}
        start = 0
        end = 0
        while end < len(s) - 1:
            end += 1
            seen[s[end]] = seen.get(s[end], 0) + 1
            if len(seen) == end - start + 1:
                best += 1
            else:
                seen[s[start]] = seen.get(s[start]) - 1
                if seen.get(s[start]) == 0:
                    del seen[s[start]]
                start += 1
        return best