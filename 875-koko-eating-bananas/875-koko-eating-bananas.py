class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        def canEat(k):
            time = 0
            for p in piles:
                time += 1 + (p - 1)//k
            return time <= h
        
        while l < r:
            mid = (l + r)//2
            if canEat(mid):
                r = mid
            
            else:
                l = mid + 1
        
        return l