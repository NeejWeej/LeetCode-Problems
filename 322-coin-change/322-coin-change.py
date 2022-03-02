class Solution:
    from collections import deque
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        seen = set()
        q = deque([amount])
        count = 0
        while q:
            count += 1
            new_layer = deque([])
            for _ in range(len(q)):
                cur = q.popleft()
                for coin in coins:
                    if cur - coin == 0:
                        return count

                    if cur - coin > 0 and cur - coin not in seen:
                        seen.add(cur - coin)
                        new_layer.append(cur - coin)
                        continue
            q = new_layer
        return -1
                
                    
                    
            
            
        
