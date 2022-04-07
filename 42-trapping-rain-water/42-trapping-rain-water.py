class Solution:
    def trap(self, height: List[int]) -> int:
        start = 0
        elev = height[start]
        ans = 0
        greatest = [float('-inf')]
        n = len(height)
        cur_max = height[-1]
        for h in range(n - 2, -1, -1):
            greatest.append(cur_max)
            cur_max = max(cur_max, height[h])    
        i = 1
        while i < n and start < n:
            if i < start:
                i = start + 1
            if i == n:
                break
            elev = min(height[start], greatest[-start - 1])
            cur = height[i]
            diff = elev - cur
            if diff > 0:
                ans += diff
            else:
                start = i
            i += 1
        return ans
            
            
                
                