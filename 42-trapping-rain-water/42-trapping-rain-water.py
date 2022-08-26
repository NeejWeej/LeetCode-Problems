class Solution:
    from itertools import islice
    
    def trap(self, height: List[int]) -> int:
        maxRight = []
        for h in reversed(height):
            if maxRight and maxRight[-1] > h:
                maxRight.append(maxRight[-1])
            else:
                maxRight.append(h)
        res = 0
        left = 0
        
        for idx, h in enumerate(height):
            if h >= left:
                left = h
                
            else:
                res += min(left, maxRight[-idx - 1]) - h
                
        return res
                
                
                