class Solution:
    from itertools import islice
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda x: x[0])
        res = [intervals[0]]
        for s,e in islice(intervals, 1, len(intervals)):
            if s <= res[-1][1]:
                res[-1][1] = max(e, res[-1][1])
            else:
                res.append([s,e])
            
        return res