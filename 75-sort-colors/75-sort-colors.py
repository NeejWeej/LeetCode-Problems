class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        top = n
        bot = -1
        start = 0
        while start < top:
            color = nums[start]
            if color == 0:
                nums[bot + 1], nums[start] = nums[start], nums[bot + 1]
                bot += 1
                if start == bot:
                    start += 1
            elif color == 2:
                nums[top - 1], nums[start] = nums[start], nums[top - 1]
                top -= 1
            elif color == 1:
                start += 1
        
            
        