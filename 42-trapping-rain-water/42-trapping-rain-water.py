class Solution:
    from itertools import islice
    def trap(self, height: List[int]) -> int:
        stack = []
        start = None
        ans = 0
        max_afterwards = [-1]
        for h in reversed(height):
            max_afterwards.append(max(h, max_afterwards[-1]))
        max_afterwards = max_afterwards[::-1]
        def popStack(start, stack, ans):
            while stack:
                s = stack.pop()
                ans += start - s
            return ans
        # print(max_afterwards)
        for i, h in enumerate(height):
            if not start:
                start = min(max_afterwards[i + 1], h)
            elif h >= start:
                ans = popStack(start, stack, ans)
                start = min(max_afterwards[i + 1], h)
            else:
                stack.append(h)  
        return ans
            
            
            
                
                