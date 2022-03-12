class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[n - 1] > nums[0]:
            return nums[0]
        start = 0
        end = n - 1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] > nums[start]:
                start = mid + 1
            else:
                end = mid
        return
        