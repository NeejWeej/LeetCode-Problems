class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        best = 0
        while left < right:
            leftH = height[left]
            rightH = height[right]
            best = max(best, min(leftH, rightH) * (right - left))
            if leftH < rightH:
                left += 1
            elif leftH == rightH:
                left += 1
                right -= 1
            else:
                right -= 1
        return best
            
        