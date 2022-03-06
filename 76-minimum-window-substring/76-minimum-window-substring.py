class Solution:
    from collections import Counter
    def minWindow(self, s: str, t: str) -> str:
        best = [float('inf'), '']
        if len(t) == 1 and t in s:
            return t
        counts = {}
        stor_counts = {}
        for c in t:
            counts[c] = 1 + counts.get(c,0)
            stor_counts[c] = 1 + stor_counts.get(c,0)
        tot_count = len(t)
        # print(counts)
        start = 0
        end = 0
        cur_counter = {}
        while end < len(s):
            cur_counter[s[end]] = 1 + cur_counter.get(s[end], 0)
            if counts.get(s[end], 0) > 0:
                counts[s[end]] = counts.get(s[end]) - 1
                tot_count -= 1
            if tot_count == 0:
                # print(start, end, cur_counter)
                while start < end:
                    if end - start + 1 < best[0]:
                        best = [end - start + 1, s[start:end + 1]]
                    if cur_counter[s[start]] <= stor_counts.get(s[start], float('-inf')):
                        break
                    cur_counter[s[start]] = cur_counter.get(s[start]) - 1
                    start += 1
            end += 1
        return best[1]
                
            