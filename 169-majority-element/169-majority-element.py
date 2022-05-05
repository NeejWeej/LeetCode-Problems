class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        total = len(nums) // 2
        return nums[total]
        