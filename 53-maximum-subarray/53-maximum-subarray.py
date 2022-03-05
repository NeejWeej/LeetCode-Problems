class Solution:
    def maxSubArray(self, nums: List[int]) -> int: 
        # cur = best = nums[0]
        # for idx in range(1, len(nums)):
        #     cur = max(cur + nums[idx], nums[idx])
        #     best = max(cur, best)
        # return best 
        
        start = 0
        end = 0
        best = nums[0]
        cur = nums[0]
        while end < len(nums) - 1:
            end += 1
            cur += nums[end]
            while start < end:
                if nums[start] < 0:
                    cur -= nums[start]
                    start += 1
                else:
                    break
            if cur <= 0:
                start = end
                cur = nums[end]
            best = max(cur, best)
        return best
            
            
                
        
        
        
        
        