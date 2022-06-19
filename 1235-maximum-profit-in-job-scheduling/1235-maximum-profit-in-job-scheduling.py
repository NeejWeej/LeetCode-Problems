class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def leftMost(jobs, curJ, endingIdx):
            startT = curJ[0]
            #find first idx where the endtime is strictly greater than our start time
            start = 0
            end = endingIdx
            while start < end:
                mid = start + (end - start)//2
                #if endtime is strictly greater, we have this as our end
                if startT < jobs[mid][0]:
                    end = mid
                elif startT >= jobs[mid][0]:
                    start = mid + 1
                # if startT <= jobs[mid][0]:
                #     start = mid + 1
                # elif startT > jobs[mid][0]:
                #     end = mid
            return start
        times = [(start, end, p) for start,end,p in zip(startTime, endTime, profit)]
        times.sort(key = lambda x: x[1])
        n = len(startTime)
        #each element of dp is [endTime, profit]
        dp = [[0, 0] for _ in range(n)]
        dp[0] = times[0][1:]
        # print(dp)
        for i in range(1, n):
            curJ = times[i]
            if curJ[0] >= dp[i-1][0]:
                #if start time is after all end times:
                dp[i] = [curJ[1], dp[i-1][1] + curJ[2]]
                continue
            leftI = leftMost(dp, curJ, i-1)
            bestWith = curJ[2]
            if leftI > 0:
                bestWith += dp[leftI - 1][1]
            if bestWith > dp[i-1][1]:
                dp[i] = [curJ[1], bestWith]
            else:
                # dp[i] = [dp[i-1][0], dp[i-1][1]]
                dp[i] = dp[i-1][:]   
        print(dp)
        return dp[-1][1]