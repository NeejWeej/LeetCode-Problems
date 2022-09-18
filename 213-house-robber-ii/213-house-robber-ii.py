class Solution:
    from itertools import islice
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        
        last = nums[1]
        last2 = nums[0]
        
        for val in itertools.islice(nums, 2, n - 1):
            last, last2 = max(val + last2, last), max(last, last2)
        
        best = max(last, last2)
        last = nums[2]
        last2 = nums[1]
        
        for val in itertools.islice(nums, 3, n):
            last, last2 = max(val + last2, last), max(last, last2)
        
        return max(best, last, last2)
            
            