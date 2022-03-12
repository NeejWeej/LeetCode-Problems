class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        stor={}
        start = 0
        best = 0
        
        for idx, ele in enumerate(s):
            if stor.get(ele, -1) < start:
                stor[ele] = idx
            else:
                if idx - start > best:
                    best = idx - start
                start = stor[ele] + 1
                stor[ele] = idx
                
        if len(s) > best + start:
            best = len(s) - start
        return best
                
        