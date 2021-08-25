class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        self.dfs(candidates, target, [], ans)
        return ans
    def dfs(self, nums, target, path, ret):
        if target == 0:
            ret.append(path)
            return
        for idx, val in enumerate(nums):
            if target < val:
                return
            self.dfs(nums[idx:], target-val, path + [val], ret)
        
            
        