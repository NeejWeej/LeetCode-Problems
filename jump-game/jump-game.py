class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False]*n
        dp[-1] = True
        for idx, val in enumerate(nums[-2::-1], 2):
            possible = False
            if val  - idx >= -1:
                possible = True
            else:
                for i in range(1,val+1):            
                    if dp[-idx + i] == True:
                        possible = True
                        break
            dp[-idx] = possible
        # print(dp)
        return dp[0]
        