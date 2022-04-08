class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        best = [float('inf'), '']
        t_counts = {}
        cur = {}
        for c in t:
            t_counts[c] = t_counts.get(c, 0) + 1
        need = len(t_counts)
        for i, c in enumerate(s):
            cur_c = cur.get(c, 0)
            cur[c] = cur_c + 1
            if cur_c == t_counts.get(c, 0) - 1:
                need -= 1
            if need == 0:
                start_letter = s[start]
                start_letter_count = cur.get(start_letter)
                while start_letter_count > t_counts.get(start_letter, 0):
                    cur[start_letter] = start_letter_count - 1
                    start += 1
                    start_letter = s[start]
                    start_letter_count = cur.get(start_letter)
                if i - start + 1 < best[0]:
                    best = [i - start + 1, s[start: i + 1]]
        return best[1]
            
                
                
            