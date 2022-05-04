class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        total = len(nums) // 2
        best = [None, -1]
        cur = nums[0]
        count = 0
        for num in nums:
            if num == cur:
                count += 1
                if count > total:
                    return num
            else:
                if best[1] < count:
                    best = [cur, count]
                cur = num
                count = 1
        return best[0]
        