class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pos = 0
        for i,v in enumerate(nums):
            if v != 0:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
        
        # nums[pos:] = [0] * (n - pos)
        
#         lastZero = n
#         curI = n - 1
#         while 0 <= curI:
#             char = nums[curI]
#             if char != 0:
#                 curI -= 1
#                 continue
                
#             for i in range(curI, lastZero - 1):
#                 nums[i],nums[i+1] = nums[i+1],nums[i]
                
#             lastZero -= 1
#             if curI >= lastZero:
#                 curI = lastZero - 1
#         return
            
            
        
        