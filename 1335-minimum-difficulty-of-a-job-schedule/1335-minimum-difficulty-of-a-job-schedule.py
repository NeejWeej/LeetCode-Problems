class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        jd = jobDifficulty
        n = len(jd)
        
        cached = {}
        def helper(start, days_left, cache):
            if (start, days_left) in cache:
                return cache.get((start, days_left))
            
            if days_left == 0:
                if start == n:
                    cache[(start, 0)] = 0
                    return 0
                cache[(start, 0)] = float('inf')
                return float('inf')
                    
            if n - start < days_left:
                cache[(start, days_left)] = float('inf')
                return float('inf')
            
            if n - start == days_left:
                val = sum(jd[start:])
                cache[(start, days_left)] = val
                return val
            
            cur_max = 0
            best_val = float('inf')
            for idx in range(start, n):
                cur_max = max(jd[idx], cur_max)
                best_val = min(best_val, cur_max + helper(idx + 1, days_left - 1, cache))
            cache[(start, days_left)] = best_val
            return best_val
                
        ans = helper(0, d, cached)
        return -1 if ans == float('inf') else ans
            