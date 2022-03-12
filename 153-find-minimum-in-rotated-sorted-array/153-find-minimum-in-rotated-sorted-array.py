class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[n - 1] > nums[0]:
            return nums[0]
        if nums[n - 2] > nums[n - 1]:
            return nums[n-1]
        start = 0
        end = n - 1
        while start < end:
            mid = start + (end - start) // 2
            print(start, mid, end)
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[mid] > nums[start]:
                start = mid + 1
            elif nums[mid] < nums[start]:
                end = mid
        return nums[start]
        