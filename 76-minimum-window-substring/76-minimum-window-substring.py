class Solution:
    from collections import Counter
    def minWindow(self, s: str, t: str) -> str:
        best = [float('inf'), '']
        if len(t) == 1 and t in s:
            return t
        counts = Counter(t)
        # print(counts)
        start = 0
        end = 0
        cur_counter = {}
        while end < len(s):
            cur_counter[s[end]] = 1 + cur_counter.get(s[end], 0)
            valid = True
            for char, num in counts.items():
                if cur_counter.get(char, 0) < num:
                    valid = False 
                    break
            if valid:
                # print(start, end, cur_counter)
                while start < end:
                    if end - start + 1 < best[0]:
                        best = [end - start + 1, s[start:end + 1]]
                    if cur_counter[s[start]] <= counts.get(s[start], float('-inf')):
                        break
                    cur_counter[s[start]] = cur_counter.get(s[start]) - 1
                    start += 1
            end += 1
        return best[1]
                
            