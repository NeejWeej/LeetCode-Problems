class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        # nums = nums[::-1]
        def subs(idx):
            if idx == n:
                return [[]]
            c = nums[idx]
            wit = subs(idx + 1)
            wio = subs(idx + 1)
            for x in wit:
                x.append(c)
            return wio + wit
        return subs(0)
                