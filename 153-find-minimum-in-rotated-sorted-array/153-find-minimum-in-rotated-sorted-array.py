class Solution:
    def findMin(self, nums: List[int]) -> int:
        # find first element smaller than first
        n = len(nums)
        left, right = 0, n
        first = nums[0]
        # if first <= nums[-1]:
        #     return nums[0]
        
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] >= first:
                left = mid + 1
            else:
                right = mid
                
        return nums[left % n]
            