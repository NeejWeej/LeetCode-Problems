class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        l = 0
        r = n
        while l < r:
            mid = (l + r) // 2
            left = float('inf') if mid == 0 else nums[mid - 1]
            right = float('inf') if mid == n - 1 else nums[mid + 1]
            
            if mid % 2 == 0:
                # should be start
                if right == nums[mid]:
                    l = mid + 1
                else:
                    r = mid
            
            else:
                if left == nums[mid]:
                    l = mid + 1
                else:
                    r = mid
        return nums[l]
                