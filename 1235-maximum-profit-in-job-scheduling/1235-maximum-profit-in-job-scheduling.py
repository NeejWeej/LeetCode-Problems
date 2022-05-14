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
            e = i - 1
            while s + 1 < e:
                mid = s + (e - s)//2
                if jobs[mid][0] <= start:
                    s = mid
                elif jobs[mid][0] > start:
                    e = mid - 1        
            if jobs[e][0] > start:
                return s
            return e
                
        dp = [[0,0] for i in range(n)]
        dp[0] = [jobs[0][1], jobs[0][2]]
        for i in range(1, n):
            start, end, profit = jobs[i]
            #last one that ends before start
            if start < dp[0][0]:
                if dp[i - 1][1] >= profit:
                    dp[i] = dp[i-1][:]
                else:
                    dp[i] = [end, profit]
                continue
            e = binSearch(dp, i, start)
            if dp[e][1] + profit > dp[i - 1][1]:
                dp[i] = [end, dp[e][1] + profit]
            else:
                dp[i] = dp[i - 1][:]
        return dp[-1][1]