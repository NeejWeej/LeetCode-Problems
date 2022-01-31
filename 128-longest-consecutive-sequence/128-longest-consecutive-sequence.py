class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        set_nums = set(nums)
        
        for num in set_nums:
            if num - 1 in set_nums:
                continue
            cur = 1
            while num + 1 in set_nums:
                cur += 1
                num += 1
            best = max(cur, best)
        return best
    
    
    
    
    
    
    
    
    
    
    
    
        # nums.sort()
        # longest, curr = 1, 1
        # last_num = nums[0]
        # direction = 0
        # for idx,val in enumerate(nums[1:], 1):
        #     if curr > longest:
        #         longest = curr
        #     if val == last_num:
        #         continue
        #     if curr == 1:
        #         if val == last_num + 1:
        #             curr += 1
        #             direction = 1
        #         elif val == last_num - 1:
        #             curr += 1
        #             direction = -1
        #         last_num = val
        #         continue
        #     if val == last_num + direction:
        #         curr += 1
        #         last_num = val
        #         continue
        #     curr = 1
        #     last_num = val
        # return max(longest,curr)
            
            
        