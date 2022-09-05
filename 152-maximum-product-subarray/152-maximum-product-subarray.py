from itertools import islice

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largeDP = smallDP = best = nums[0]
        for num in (val for i,val in enumerate(nums) if i > 0):
            candidates = sorted([num, smallDP * num, largeDP*num])
            largeDP = candidates[-1]
            smallDP = candidates[0]
            if best < largeDP:
                best = largeDP
        
        return best
                