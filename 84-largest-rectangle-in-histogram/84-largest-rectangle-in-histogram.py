class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        rightExtend = [0] * n
        
        for i,v in enumerate(heights):
            while stack and v < stack[-1][1]:
                idx, lastVal = stack.pop()
                rightExtend[idx] = i - idx
            stack.append((i, v))
        
        while stack:
            idx, lastVal = stack.pop()
            rightExtend[idx] = n - idx 
            
        leftExtend = [0] * n
        
        for i,v in enumerate(reversed(heights)):
            while stack and v < stack[-1][1]:
                idx, lastVal = stack.pop()
                leftExtend[idx] = i - idx
            stack.append((i, v))
        
        while stack:
            idx, lastVal = stack.pop()
            leftExtend[idx] = n - idx 
            
        vals = [h*(leftExtend[-i-1] + rightExtend[i] - 1) for i,h in enumerate(heights)]
        return max(vals)
            
        
            
            