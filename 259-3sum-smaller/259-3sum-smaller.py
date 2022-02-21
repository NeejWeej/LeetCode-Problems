class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for idx in range(n):
            cur_val = nums[idx]
            start = idx + 1
            end = n - 1
            while start < end:
                cur_sum = nums[start] + nums[end] + cur_val
                if cur_sum < target:
                    ans += (end - start)
                    start += 1  
                elif cur_sum >= target:
                    end -= 1
                    continue
        return ans
                
                
                