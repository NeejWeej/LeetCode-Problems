from itertools import islice

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        largeDP = smallDP = best = nums[0]
        for num in islice(nums, 1, len(nums)):
            candidates = sorted([num, smallDP * num, largeDP*num])
            largeDP = candidates[-1]
            smallDP = candidates[0]
            # if best < largeDP:
            #     best = largeDP
            best = max(largeDP, best)
        
        return best
                