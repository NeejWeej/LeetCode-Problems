# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        if isBadVersion(1):
            return start
        while start < end:
            mid = start + (end - start) // 2
            mid_val = isBadVersion(mid)
            prev_v = isBadVersion(mid - 1)
            if not prev_v and mid_val:
                return mid 
            if not mid_val:
                start = mid + 1
            elif mid_val:
                end = mid
        return start