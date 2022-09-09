class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        n = len(temp)
        ans = [0 for _ in range(n)]
        stack = []
        
        for i,t in enumerate(temp):
            while stack and t > stack[-1][0]:
                oldT, idx = stack.pop()
                ans[idx] = i - idx
            stack.append((t, i))
        
        return ans
            
            
                
                
            