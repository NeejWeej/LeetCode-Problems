class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        times = []
        n = len(timePoints)
        if n >= 24*60:
            return 0
        for time in timePoints:
            hr, minutes = time.split(':')
            times.append(int(hr)*60 + int(minutes))
        
        times.sort()
        best = float('inf')
        
        for i in range(n - 1):
            cur, nextt = times[i: i+2]
            possib = nextt - cur
            best = min(best, possib)
        return min(best, times[0] + 24*60 - times[-1])