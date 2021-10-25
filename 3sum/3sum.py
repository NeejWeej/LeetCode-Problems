class Solution(object):
    def threeSum(self,nums):
        n = len(nums)
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        ans = set()
        
        for idx, val in enumerate(nums):
            counts[val] -= 1
            if counts[val] <= 0:
                counts.pop(val)
            
            for num, count in counts.items():
                if -val - num == num:
                    if -val-num in counts and count > 1:
                        new = [num, val, -val-num]
                        new.sort()
                        ans.add(tuple(new))                    
                    
                elif -val-num in counts:
                    new = [num, val, -val-num]
                    new.sort()
                    ans.add(tuple(new))
        
        return list(ans)
        
        
        
        
        
        # nums.sort()
        # res = set()
        # for idx, val in enumerate(nums):
        #     #since sorted, we will only run into repeats in a continguous block
        #     if idx != 0 and val == nums[idx-1]:
        #         continue
        #     if idx >= n-2:
        #         break
        #     sums = set()
        #     m = nums[idx+1:]
        #     for i,v in enumerate(m):
        #         if -val-v in sums:
        #             res.add((-val-v,val,v))
        #         else:
        #             sums.add(v)
        # return res
