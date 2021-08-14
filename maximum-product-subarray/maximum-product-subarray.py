class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_prod = min_prod = nums[0]
        best = nums[0]
        for val in nums[1:]:
            candidates = (val, min_prod*val, max_prod*val)
            max_prod = max(candidates)
            min_prod = min(candidates)
            if max_prod > best:
                best = max_prod
        return best