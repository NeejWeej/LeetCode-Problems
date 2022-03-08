class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        before = 0
        bbefore = 0
        for i in range(2, n + 1):
            before, bbefore = min(before + cost[i-1], bbefore + cost[i - 2]), before
        return before