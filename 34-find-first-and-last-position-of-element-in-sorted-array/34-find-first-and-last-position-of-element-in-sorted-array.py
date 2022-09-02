class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)
        ans = [-1, -1]
        if not nums or target < nums[0] or nums[-1] < target:
            return ans
        
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] < target:
                l = mid + 1
                
            else:
                r = mid
        if nums[l] != target:
            return ans
        
        ans[0] = l
        r = len(nums)
        while l < r:
            mid = (l + r)//2
            
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid
                
        ans[1] = l - 1
        return ans
        
        
        
            