class Solution:
        
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        end_uniq = 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[end_uniq]:
                end_uniq += 1
                nums[end_uniq] = nums[i]
        return end_uniq + 1
                