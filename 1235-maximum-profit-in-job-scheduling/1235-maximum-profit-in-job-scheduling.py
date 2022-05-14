class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        jobs = [
            (startTime[i], endTime[i], profit[i])
            for i in range(n)
        ]
        jobs.sort(key = lambda x: x[1])
        def binSearch(jobs, i, start):
            s = 0
            e = i
            while s < e:
                mid = s + (e - s)//2
                if jobs[mid][0] <= start:
                    s = mid + 1
                else:
                    e = mid        
            return s
                
        dp = [[0,0] for i in range(n)]
        dp[0] = [jobs[0][1], jobs[0][2]]
        for i in range(1, n):
            start, end, profit = jobs[i]
            #first one that ends strictly after start
            e = binSearch(dp, i, start) - 1
            compatible_best = dp[e][1] if e >= 0 else 0 
            if compatible_best + profit > dp[i - 1][1]:
                dp[i] = [end, compatible_best + profit]
            else:
                dp[i] = dp[i - 1][:]
        return dp[-1][1]