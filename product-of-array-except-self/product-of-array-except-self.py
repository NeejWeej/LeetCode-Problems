class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1]*n
        for idx, val in enumerate(nums[1:],1):
            #store product of all values to the left of that number
            answer[idx] = answer[idx-1]*nums[idx-1]
        right_product = 1
        for i in range(n-1,-1,-1):
            answer[i] *= right_product
            right_product *= nums[i]
        return answer
        
        