class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for idx, dig in enumerate(reversed(nums)):
            new_idx = -idx - 1
            if new_idx == -1:
                continue
            if dig >= nums[new_idx + 1]:
                continue
            # nums[new_idx + 1], nums[new_idx] = nums[new_idx], nums[new_idx + 1]
            # return
            i = -1
            while True:
                if nums[i] > dig:
                    nums[i], nums[new_idx] = nums[new_idx], nums[i]
                    break
                i -= 1
            shift = new_idx + 1 + n 
            len_from_end = abs(new_idx + 1)
            for i in range(len_from_end // 2):
                new_i = shift + i
                nums[new_i], nums[-i - 1] = nums[-i - 1], nums[new_i]
            return
        for i in range(n // 2):
            nums[i], nums[-i-1] = nums[-i-1], nums[i]
        return
            
        