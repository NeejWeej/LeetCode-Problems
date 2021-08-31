class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def get_median(vals):
            s_vals = sorted(vals)
            if len(s_vals)%2 == 1:
                return s_vals[len(vals)//2]
            return (s_vals[len(vals)//2] + s_vals[len(vals)//2 - 1])/2
        
        cur_vals = nums[:k]
        output = []
        for i in range(k, len(nums)):
            output.append(get_median(cur_vals))
            cur_vals.pop(0)
            cur_vals.append(nums[i])
        output.append(get_median(cur_vals))
        return output
        # deq = collections.deque([])
        # for idx, val in enumerate(nums):
            
        
        