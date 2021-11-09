class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # def factorial(x):
        #     ans = 1
        #     while x > 0:
        #         ans *= x
        #         x -= 1
        #     return ans
        n = len(nums)
        if n == 1:
            return [nums]
        old_ans = self.permute(nums[1:])
        to_add = nums[0]
        new_ans = []
        for idx in range(n):
            for perm in old_ans:
                new_perm = []
                for i in range(n):
                    if i < idx:
                        new_perm.append(perm[i])
                    elif i == idx:
                        new_perm.append(to_add)
                    else:
                        new_perm.append(perm[i - 1])
                new_ans.append(new_perm)
        return new_ans
        # fac_n = factorial(n)
        # ans = [[0 for _ in range(n)] for __ in range(fac_n)]