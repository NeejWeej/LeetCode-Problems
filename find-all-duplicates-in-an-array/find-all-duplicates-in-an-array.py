class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for idx, val in enumerate(nums):
            val = abs(val)
            if nums[val-1] > 0:
                nums[val-1] *= -1
            elif nums[val-1] < 0:
                res.append(val)
        return res
                
        