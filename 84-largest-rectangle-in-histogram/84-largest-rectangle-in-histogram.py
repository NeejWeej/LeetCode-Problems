class Solution:
    from collections import deque
    def largestRectangleArea(self, heights: List[int]) -> int:
        deq = deque([])
        n = len(heights)
        rightExtend = [0] * n
        for i,v in enumerate(heights):
            while len(deq) > 0 and v < deq[-1][1]:
                idx, lastVal = deq.pop()
                rightExtend[idx] = i - idx
            deq.append((i, v))
        
        while len(deq) > 0:
            idx, lastVal = deq.pop()
            rightExtend[idx] = n - idx 
            
        leftExtend = [0] * n
        
        for i,v in enumerate(reversed(heights)):
            while len(deq) > 0 and v < deq[-1][1]:
                idx, lastVal = deq.pop()
                leftExtend[idx] = i - idx
            deq.append((i, v))
        
        while len(deq) > 0:
            idx, lastVal = deq.pop()
            leftExtend[idx] = n - idx 
            
        vals = [h*(leftExtend[-i-1] + rightExtend[i] - 1) for i,h in enumerate(heights)]
        return max(vals)
            
        
            
            