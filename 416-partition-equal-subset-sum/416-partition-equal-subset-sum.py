class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        n = len(nums)
        if total % 2 == 1: return False
        dp = {}
        def diff(d, idx):
            if idx == n - 1:
                if d == nums[n-1] or d == -nums[n-1]: 
                    dp[(d, idx)] = True
                else:
                    dp[(d, idx)] = False
            else:
                cur_num = nums[idx]
                do_plus = True
                do_minus = True
                if (d - cur_num, idx + 1) in dp:
                    do_minus = False
                    if dp.get((d - cur_num, idx + 1)):
                        dp[(d, idx)] = True
                        return
                if (d + cur_num, idx + 1) in dp:
                    do_plus = False
                    if dp.get((d + cur_num, idx + 1)):
                        dp[(d, idx)] = True
                        return
                if do_plus:
                    diff(d + cur_num, idx + 1)
                    if dp.get((d + cur_num, idx + 1)):
                        dp[(d, idx)] = True
                        return
                if do_minus:
                    diff(d - cur_num, idx + 1)
                    if dp.get((d - cur_num, idx + 1)):
                        dp[(d, idx)] = True
                        return
                dp[(d, idx)] = False
                return
        diff(0, 0)
        # print(dp)
        return dp.get((0,0))
                
            