class Solution:
    
    def can_complete(self, piles, h, k):
        cur_hours = 0
        for pile in piles:
            cur_hours += (pile // k)
            if pile % k != 0:
                cur_hours += 1
            if cur_hours > h:
                return False
        return True
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if self.can_complete(piles, h, 1):
            return 1
        cannot = 1
        can = cannot
        while True:
            can = can << 1
            if self.can_complete(piles, h, can):
                break
            cannot = can
        start = cannot
        end = can
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.can_complete(piles, h, mid):
                end = mid
            else:
                start = mid
        if self.can_complete(piles, h, start):
            return start
        return end
        
        
        