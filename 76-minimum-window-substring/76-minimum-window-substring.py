class Solution:
    from collections import Counter
    def minWindow(self, s: str, t: str) -> str:
        if len(t) == 1 and t in s:
            return t
        best = None
        tCounts = Counter(t)
        cur_chars = {}
        cur_completed = 0
        start = 0
        end = 0
        for idx, c in enumerate(s):
            cur_val = cur_chars.get(c, 0)
            cur_chars[c] = cur_val + 1
            if cur_val == tCounts.get(c, 0) - 1:
                cur_completed += 1
            if cur_completed != len(tCounts):
                continue
            schar = s[start]
            while cur_chars.get(schar) > tCounts.get(schar, 0):
                cur_chars[schar] = cur_chars.get(schar) - 1
                start += 1
                schar = s[start]
            if not best:
                best = s[start: idx + 1]
            elif len(best) > len(s[start: idx + 1]):
                best = s[start: idx + 1]
        # print(tCounts, cur_chars, s[start:])
        return best if best else ""
            
                
                
                
            