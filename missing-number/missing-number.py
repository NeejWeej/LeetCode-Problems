class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        actual_sum = sum(nums)
        supposed_sum = (n * (n + 1)) >> 1
        return supposed_sum - actual_sum