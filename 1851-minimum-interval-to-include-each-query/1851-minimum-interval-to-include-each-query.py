import heapq as hq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        qDict = {}
        intervals.sort(key=lambda x: x[0])
        # get earliest starting intervals
        validIntervals = []
        n = len(intervals)
        idx = 0
        # interval is valid for a contiguous portion
        
        for q in sorted(queries):
            while idx < n and intervals[idx][0] <= q:
                s,e = intervals[idx]
                if e >= q:
                    tup = (e - s + 1, s, e)
                    hq.heappush(validIntervals, tup)
                idx += 1
                
            while validIntervals:
                length, s, e = validIntervals[0]
                if s <= q <= e:
                    qDict[q] = length
                    break
                hq.heappop(validIntervals)
                
            if not validIntervals:
                qDict[q] = -1          
                
        return [qDict[q] for q in queries]
                
            