class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = 0
        n = len(nums)
        end = n - 1
        
        while True:
            mid = start + ((end - start) // 2)
            greater_than_left = False
            if mid == 0 or nums[mid - 1] < nums[mid]:
                greater_than_left = True
            greater_than_right = False
            
            if mid == n - 1 or nums[mid + 1] < nums[mid]:
                greater_than_right = True
            
            if greater_than_left and greater_than_right:
                return mid
            
            if not greater_than_left:
                end = mid - 1
            
            else:
                start = mid + 1
        return
                
                