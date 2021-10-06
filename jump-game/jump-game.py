class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        we keep track of the lowest index that is still possible to reach the end with
        We use negative indices so that we can loop through the list in reverse
        '''
        # n, last_possible = len(nums), -1
        # for idx, val in enumerate(nums[-2::-1], 2):
        #     if val - idx >= last_possible:
        #         last_possible = -idx
        # return last_possible == -n
        
        '''
        below we reverse the list, and thus use positive indices
        '''
        n = len(nums)
        last_possible = n -1 
        for i in reversed(range(n)):
            if nums[i] + i >= last_possible:
                last_possible = i
        return last_possible == 0
        
        
        # n, last_possible = len(nums), 0
        # reverse_nums = nums[::-1]
        # for idx, val in enumerate(reverse_nums):
        #     if idx - val <= last_possible:
        #         last_possible = idx
        # return last_possible == n-1
        