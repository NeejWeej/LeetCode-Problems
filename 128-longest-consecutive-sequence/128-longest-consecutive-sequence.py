class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        best = 0
        seen = {}
        
        def storeLongestPath(pathL, num, numSet):
            if num in pathL or num not in numSet:
                return pathL.get(num, 0)
            val = storeLongestPath(pathL, num + 1, numSet)
            pathL[num] = val + 1
            return val + 1
            
        for num in nums:
            best = max(best, storeLongestPath(seen, num, numSet))
        return best
        