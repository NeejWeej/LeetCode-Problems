class Solution:
    from itertools import islice
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = set([])
        for idx, num in enumerate(islice(nums, 0, n - 2)):
            l = idx + 1
            r = n - 1
            while l < r:
                leftPlusRight = nums[l] + nums[r]
                if leftPlusRight == -num:
                    ans.add((num, nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif leftPlusRight + num < 0:
                    l += 1
                    
                else:
                    # leftPlusRight + num > 0
                    r -= 1
        return ans
                