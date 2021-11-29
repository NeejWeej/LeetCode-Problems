class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        left_one = [0 for _ in range(len(s))]
        for i in range(1, len(s)):
            left_one[i] = left_one[i - 1]
            if s[i - 1] == '1':
                left_one[i] += 1
        right_zero = [0 for _ in range(len(s))]
        
        for i in range(len(s) - 2, -1, -1):
            right_zero[i] = right_zero[i + 1]
            if s[i + 1] == '0':
                right_zero[i] += 1
        
        best = float('inf')
        for i in range(len(s)):
            min_change_i = left_one[i] + right_zero[i]
            best = min(min_change_i, best)
        return best
            