class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = height[0]
        right_max = height[right]
        
        ans = 0
        while left <= right:
            if left_max <= height[left]:
                left_max = height[left]
                left += 1
                continue
                
            if right_max <= height[right]:
                right_max = height[right]
                right -= 1
                continue
            
            if left_max <= right_max:
                ans += max(0, left_max - height[left])
                left += 1
                continue
            
            ans += max(0, right_max - height[right])
            right -= 1
        return ans
            
                
                