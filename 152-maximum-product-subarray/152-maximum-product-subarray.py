from itertools import islice

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largeDP = smallDP = best = nums[0]
        for num in islice(nums, 1, len(nums)):
            largeNew = max(num, smallDP * num, largeDP * num)
            smallNew = min(num, smallDP * num, largeDP * num)
            largeDP, smallDP = largeNew, smallNew
            best = max(largeDP, best)
        
        return best
                