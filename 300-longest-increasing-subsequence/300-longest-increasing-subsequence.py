class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def binSearch(toFind, vals):
            left = 0
            right = len(vals)
            while left < right:
                mid = (left + right)// 2
                midVal = vals[mid]
                if midVal < toFind:
                    left = mid + 1
                else:
                    right = mid
            return left
            
        
        n = len(nums)
        best = []
        for num in nums:
            if not best or best[-1] < num:
                best.append(num)
            else:
                idx = binSearch(num, best)
                best[idx] = num
        return len(best)