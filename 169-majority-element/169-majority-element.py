class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = nums[0]
        count = 0
        for num in nums:
            if count == 0:
                cur = num
            count += (1 if num == cur else -1)
        return cur
        