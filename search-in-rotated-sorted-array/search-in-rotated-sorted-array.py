class Solution:
    def search(self, nums: List[int], target: int) -> int:
        max_right = nums[-1]
        min_left = nums[0]
        
        if target == max_right:
            return len(nums) - 1 
        
        if target == min_left:
            return 0
        
        start = 0
        end = len(nums) - 1
        
        while start < end:
            mid = start + (end-start)//2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] > nums[mid + 1]:
                start = mid
                break
            
            if nums[mid] < max_right:
                end = mid
                continue
                
            if nums[mid] > min_left:
                start = mid + 1      
        rot_idx = start
        print(start, end)
        #so then num[0] is actually num[rot_idx] if sorted
        if rot_idx == 0:
            start = 0
            end = len(nums) - 1
            
        elif target > min_left:
            start = 0
            end = rot_idx
        
        elif target < max_right:
            start = rot_idx
            end = len(nums) - 1
        
        while start < end:
            mid = start + (end-start)//2
            
            if nums[mid] == target:
                return mid
            
            if target < nums[mid]:
                end = mid - 1
                
            elif target > nums[mid]:
                start = mid + 1
        
        return -1 if nums[start] != target else start
        
            
                
        