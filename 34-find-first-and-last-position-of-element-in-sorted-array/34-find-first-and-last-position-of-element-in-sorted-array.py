class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        def findFirst(num, nums):
            l = 0
            r = len(nums)
            if nums[-1] < num:
                return -1
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            return l if nums[l] == num else -1
        
        def findLast(num, nums):
            l = 0
            r = len(nums)
            if num < nums[0]:
                return -1
            
            while l < r:
                mid = (l + r) // 2
                if nums[mid] <= num:
                    l = mid + 1
                else:
                    r = mid
                    
            return l - 1 if nums[l - 1] == num else -1
        
        return [findFirst(target, nums), findLast(target, nums)]