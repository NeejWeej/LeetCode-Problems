class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if target < nums[0]:
            return -1
        l = 0
        r = n - 1
        while l < r:
            m = l + (r - l)//2
            mid = nums[m]
            if mid == target:
                return m
            elif mid < target:
                l = m + 1
            else:
                r = m - 1
        return -1 if nums[l] != target else l
        