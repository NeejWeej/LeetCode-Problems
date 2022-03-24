class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        ans = [intervals[0]]
        idx = 1
        while idx < len(intervals):
            start, end = intervals[idx][:]
            cur_end = ans[-1][-1]
            if start <= cur_end:
                ans[-1][-1] = max(end, cur_end)
            else:
                ans.append([start, end])
            idx += 1
        return ans