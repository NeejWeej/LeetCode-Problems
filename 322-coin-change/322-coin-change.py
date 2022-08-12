class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        vals = [float('inf') for _ in range(amount + 1)]
        for c in coins:
            if c > amount:
                continue
                
            vals[c] = 1
            for i in range(c + 1, amount + 1):
                vals[i] = min(vals[i - c] + 1, vals[i])
        return vals[amount] if vals[amount] != float('inf') else -1
        