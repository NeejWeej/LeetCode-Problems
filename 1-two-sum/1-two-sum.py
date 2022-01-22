class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list = [(idx, val) for idx, val in enumerate(nums)]
        new_list.sort(key = lambda x: x[1])
        # print(new_list, nums)
        start = 0
        end = len(nums) - 1
        
        cur_left = new_list[start][1]
        cur_right = new_list[end][1]
        # [2, 7, 11, 15] cur_left = 2, cur_right = 15
        
        while True:
            cur_left = new_list[start][1]
            cur_right = new_list[end][1]
            
            if cur_left + cur_right == target:
                return [new_list[start][0], new_list[end][0]]

            if cur_left + cur_right < target:
                start += 1

            if cur_left + cur_right > target:
                end -= 1
        
        
        
        # sums = {}
        # for idx, val in enumerate(nums):
        #     if target-val in sums:
        #         return [idx, sums.get(target-val)]
        #     sums[val] = idx
        # return 'Error'