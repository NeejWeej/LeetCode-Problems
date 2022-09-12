class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pivot is first number less than start
        # it is also minimum
        n = len(nums)
        # if n == 1:
            
        l, r = 0, n
        start = nums[0]
        
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < start:
                r = mid
            elif nums[mid] >= start:
                l = mid + 1
    
        # so if pivot n, go to 0 cause thats the minimum
        pivot = l % n
        
        lB, rB = 0, pivot
        lS, rS = pivot, n
        
        while lB < rB:
            mid = (lB + rB) // 2
            if nums[mid] < target:
                lB = mid + 1
            elif nums[mid] >= target:
                rB = mid
                
        if nums[lB] == target:
            return lB
        
        while lS < rS:
            mid = (lS + rS) // 2
            if nums[mid] < target:
                lS = mid + 1
            elif nums[mid] >= target:
                rS = mid 
        
        if lS != n and nums[lS] == target:
            return lS
        
        return -1
            
            
            
        