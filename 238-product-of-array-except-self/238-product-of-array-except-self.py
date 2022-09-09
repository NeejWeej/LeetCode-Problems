class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProd = [1 for _ in range(n)]
        
        for i in range(1, n):
            leftProd[i] = leftProd[i - 1] * nums[i - 1]
        
        # do rightProd
        fromRight = 1
        for i in range(n - 1, -1, -1):
            leftProd[i] *= fromRight
            fromRight *= nums[i]
        
        return leftProd
            
        