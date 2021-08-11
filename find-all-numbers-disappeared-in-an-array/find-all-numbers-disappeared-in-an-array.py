class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_storage = set()
        for num in nums:
            num_storage.add(num)
        res = []
        for num in range(1,n+1):
            if num not in num_storage:
                res.append(num)
        return res
        