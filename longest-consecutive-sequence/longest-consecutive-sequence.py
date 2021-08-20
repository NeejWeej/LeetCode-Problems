class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest, curr = 1, 1
        last_num = nums[0]
        direction = 0
        for idx,val in enumerate(nums[1:], 1):
            if curr > longest:
                longest = curr
            if val == last_num:
                continue
            if curr == 1:
                if val == last_num + 1:
                    curr += 1
                    direction = 1
                elif val == last_num - 1:
                    curr += 1
                    direction = -1
                last_num = val
                continue
            if val == last_num + direction:
                curr += 1
                last_num = val
                continue
            curr = 1
            last_num = val
        return max(longest,curr)
            
            
        