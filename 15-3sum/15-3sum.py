class Solution(object):
    def threeSum(self,nums):
        n = len(nums)
        nums.sort()
        cur_idx = 0
        ans = set()
        while cur_idx < n:
            val = nums[cur_idx]
            start = cur_idx + 1
            end = n - 1
            while start < end:
                triplet_val = nums[start] + nums[end] + val
                if triplet_val == 0:
                    ans.add((val, nums[start], nums[end]))
                    start += 1
                elif triplet_val < 0:
                    start += 1
                elif triplet_val > 0:
                    end -= 1
            cur_idx += 1
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         n = len(nums)
#         counts = {}
#         for num in nums:
#             counts[num] = counts.get(num, 0) + 1
        
#         ans = set()
        
#         for idx, val in enumerate(nums):
#             counts[val] -= 1
#             if counts[val] <= 0:
#                 counts.pop(val)
            
#             for num, count in counts.items():
#                 if -val - num == num:
#                     if count > 1:
#                         new = [num, val, -val-num]
#                         new.sort()
#                         ans.add(tuple(new))                    
                    
#                 elif -val-num in counts:
#                     new = [num, val, -val-num]
#                     new.sort()
#                     ans.add(tuple(new))
        
#         return list(ans)
        
