class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        start = 0
        for num in nums:
            start ^= num
        return start
        