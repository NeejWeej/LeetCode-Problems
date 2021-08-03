class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sums = {}
        for idx, val in enumerate(nums):
            if target-val in sums:
                return [idx, sums.get(target-val)]
            sums[val] = idx
        return 'Error'