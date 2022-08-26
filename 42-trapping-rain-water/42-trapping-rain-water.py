class Solution:
    from collections import deque
    
    def trap(self, height: List[int]) -> int:
        maxRight = deque([])
        
        for h in reversed(height):
            if maxRight and maxRight[0] > h:
                maxRight.appendleft(maxRight[0])
            else:
                maxRight.appendleft(h)
                
        res = 0
        left = 0
        for h in height:
            right = maxRight.popleft()
            if h >= left:
                left = h 
            else:
                res += min(left, right) - h
                
        return res
                
                
                