from collections import OrderedDict
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for idx, val in enumerate(nums):
            if val < 0:
                nums[idx] = 0
                
        for idx, val in enumerate(nums):
            if val != 'e' and abs(val) <= n and val != 0:
                abs_val = abs(val)
                if nums[abs_val - 1] == 'e':
                    continue
                if nums[abs_val - 1] > 0:
                    nums[abs_val - 1] *= -1
                elif nums[abs_val - 1] == 0:
                    nums[abs_val - 1] = 'e'
                    
        for idx, val in enumerate(nums):
            if val != 'e' and val >= 0:
                return idx + 1
        return n + 1
            
        