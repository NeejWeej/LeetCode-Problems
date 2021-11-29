class Solution(object):
    def threeSum(self,nums):
        n = len(nums)
        nums.sort()
        
        ans = set()
        
        # counts = {}
        # for num in nums:
        #     counts[num] = counts.get(num,0) + 1
        
        seen = set()
        
        for i in range(n):
            cur_num = nums[i]
            if cur_num in seen:
                continue
            # counts[cur_num] -= 1
            # if counts[cur_num] <= 0:
            #     del counts[cur_num]           
            left = i + 1
            right = n - 1
            while left < right:
                new_sum =  nums[left] + nums[right] + cur_num
                if new_sum == 0:
                    ans.add((cur_num, nums[left], nums[right]))
                    left += 1 
                elif new_sum < 0:
                    left += 1   
                elif new_sum > 0:
                    right -= 1
            seen.add(cur_num)
        return list(ans)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
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
        
