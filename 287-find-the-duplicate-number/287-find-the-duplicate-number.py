class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        
        def check(val):
            count = 0
            for num in nums:
                if num <= val:
                    count += 1
            return count <= val
        
        left, right = 1, n
        
        while left < right:
            mid = left + (right - left)//2
            if check(mid):
                left = mid + 1
            else:
                right = mid
        return left