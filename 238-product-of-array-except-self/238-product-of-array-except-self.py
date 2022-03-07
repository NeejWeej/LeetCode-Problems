class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [1 for _ in range(n)]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        left = [1 for _ in range(n)]
        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        return [x * y for x,y in zip(right, left)]
        
        
        
        
        
        