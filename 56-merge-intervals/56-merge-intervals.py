class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda x: x[0])
        results = [intervals[0]]
        for idx, val in enumerate(intervals):
            if val[0] <= results[-1][1]: 
                results[-1][1] = max(val[1], results[-1][1])
            else:
                results.append(val)
        return results