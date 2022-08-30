class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(cost)
        best, bestIdx = float('-inf'), -1
        cur = 0
        for i in range(n-1, -1, -1):
            cur += gas[i] - cost[i]
            if cur > best:
                best, bestIdx = cur, i
        return bestIdx if cur >= 0 else -1
            