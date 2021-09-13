class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals_tup = [(pair[0],pair[1]) for pair in intervals]
        intervals_tup.sort(key = lambda x : x[1])
        total = len(intervals_tup)
        pair = intervals_tup[0]
        cur_end = pair[1]
        count = 1
        for pair in intervals_tup:
            if pair[0] < cur_end:
                continue
            count += 1
            cur_end = pair[1]
        return total - count
            