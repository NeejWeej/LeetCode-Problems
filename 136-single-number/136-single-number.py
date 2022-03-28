class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        start = 0
        for num in nums:
            start ^= num
        return start
        