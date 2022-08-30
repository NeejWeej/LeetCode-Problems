class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        toEnd = n-1
        
        for revidx, val in enumerate(reversed(nums)):
            idx = n - revidx - 1
            if idx + val >= toEnd:
                toEnd = idx
                
        return toEnd == 0