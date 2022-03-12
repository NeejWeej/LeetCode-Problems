class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        stor={}
        for i in s:
            if i not in stor:
                stor[i] = -1
        start = 0
        best = 0
        
        for idx, ele in enumerate(s):
            if stor[ele] < start:
                stor[ele] = idx
                continue
            if idx - start > best:
                best = idx - start
            start = stor[ele] + 1
            stor[ele] = idx
                
        if len(s) > best + start:
            best = len(s) - start
        return best
                
        