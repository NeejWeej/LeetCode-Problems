class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        l = 0
        r = n
        while l < r:
            mid = (l + r) // 2
            left = float('inf') if mid == 0 else nums[mid - 1]
            right = float('inf') if mid == n - 1 else nums[mid + 1]
            leftEq = left == nums[mid]
            rightEq = right == nums[mid]
            
            if not leftEq and not rightEq:
                return nums[mid]
            
            if mid % 2 == 0:
                # should be start
                if rightEq:
                    l = mid + 1
                else:
                    r = mid - 1
            
            else:
                if leftEq:
                    l = mid + 1
                else:
                    r = mid - 1
        return nums[l]
                