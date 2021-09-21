class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        left = 1
        right = 1
        for i, val in enumerate(nums):
            ans[i] *= left
            left *= val
        
        for i in reversed(range(n)):
            ans[i] *= right
            right *= nums[i]
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(nums)
        # left_product = 1
        # right_product = 1
        # answer = [1]*n
        # for i, val in enumerate(nums):
        #     answer[i] *= left_product
        #     answer[-1-i] *= right_product
        #     right_product *= nums[-1-i]
        #     left_product *= val
        # return answer
        
        