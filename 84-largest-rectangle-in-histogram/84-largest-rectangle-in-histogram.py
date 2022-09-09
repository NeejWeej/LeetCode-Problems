class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0, -1)]
        n = len(heights)
        best = 0
        for i,h in enumerate(heights):
            while h < stack[-1][0]:
                oldH, idx = stack.pop()
                idxBefore = stack[-1][1]
                best = max(best, oldH *(i - idxBefore - 1))
            stack.append((h, i))
        
        for i in range(1, len(stack)):
            h = stack[i][0]
            last = stack[i-1][1]
            best = max(best, h * (n - 1 - last))
        
        return best
                
                
#         rightExtend = [0] * n
        
#         for i,v in enumerate(heights):
#             while stack and v < stack[-1][1]:
#                 idx, lastVal = stack.pop()
#                 rightExtend[idx] = i - idx
#             stack.append((i, v))
        
#         while stack:
#             idx, lastVal = stack.pop()
#             rightExtend[idx] = n - idx 
        
#         ans = 0
#         for i,v in enumerate(reversed(heights)):
#             while stack and v < stack[-1][1]:
#                 idx, lastVal = stack.pop()
#                 ans = max(ans, lastVal *(i - idx - 1 + rightExtend[-idx-1]))
#             stack.append((i,v))
#         while stack:
#             idx, lastVal = stack.pop()
#             ans = max(ans, lastVal * (n - idx - 1 + rightExtend[-idx-1]))
            
#         return ans
            
        
            
            