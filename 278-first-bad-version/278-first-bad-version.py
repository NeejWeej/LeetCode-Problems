# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        while start < end - 1:
            mid = start + (end - start) // 2
            mid_val = isBadVersion(mid)
            if not mid_val:
                start = mid
            elif mid_val:
                end = mid
        if isBadVersion(start):
            return start
        return end