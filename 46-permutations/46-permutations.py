class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # def factorial(x):
        #     if x == 1:
        #         return 1
        #     return x * factorial(x-1)
        # total = [list() for _ in range(factorial(len(nums) - 1))]
        # print('hi', nums[:0], nums[len(nums):], ' asf')
        n = len(nums)
        if n == 1:
            return [nums]
        oldPermutes = self.permute(nums[1:])
        newPermutes = []
        top = nums[0]
        for op in oldPermutes:
            for i in range(n - 1):
                newList = op[:i] + [top] + op[i:]
                newPermutes.append(newList)
            op.append(top)
            newPermutes.append(op)
        return newPermutes
            
        
                                       