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
            if mid == n:
                return mid
            mid_val = isBadVersion(mid)
            next_v = isBadVersion(mid + 1)
            if mid_val and not next_v:
                return mid + 1
            if not mid_val:
                start = mid + 1
            elif mid_val:
                end = mid
        return start