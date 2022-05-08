class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {0:0, 1:0, 2:0}
        for num in nums:
            d[num] += 1
        d[1] += d[0]
        d[2] += d[1]
        for i in range(len(nums)):
            if i < d[0]:
                nums[i] = 0
            elif i < d[1]:
                nums[i] = 1
            else:
                nums[i] = 2
        return nums