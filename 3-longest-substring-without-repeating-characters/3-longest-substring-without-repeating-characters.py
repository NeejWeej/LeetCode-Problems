class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        stor={i:-1 for i in s}
        
        start = 0
        best = 0
        
        for idx, ele in enumerate(s):
            if stor[ele] < start:
                stor[ele] = idx
            else:
                if idx - start > best:
                    best = idx - start
                start = stor[ele] + 1
                stor[ele] = idx
        return max(best, len(s) - start)
                
        