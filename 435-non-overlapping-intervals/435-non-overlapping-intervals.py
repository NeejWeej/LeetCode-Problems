class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        start = intervals[0][0]
        count = 0
        for interval in intervals:
            if interval[0] >= start:
                start = interval[1]
            else:
                count += 1
        return count
            