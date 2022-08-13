class Solution:
    import bisect
    import itertools
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = [[float('inf'), 0] for _ in range(n)]
        tickets = [1, 7, 30]
        costVals = list(map(tuple, zip(costs, [-1, -7, -30])))
        cost, duration = sorted(costVals, key= lambda x: x[0])[0]
        dp[0] = [cost, -duration - 1]
        for i,d in enumerate(itertools.islice(days, 1, n), 1):
            # we can extend day before without any worries
            if d - days[i - 1] <= dp[i-1][1]:
                dp[i] = [dp[i-1][0], dp[i-1][1] - (d - days[i-1])]
            else:
                min_so_far = [float('inf'), 0]
                for duration, price in zip(tickets, costs):
                    idx = bisect.bisect_left(days, d - duration + 1, lo=0, hi=i + 1)
                    prev = dp[idx-1][0] if idx > 0 else 0
                    new_min = prev + price
                    new_dur = days[idx] + duration - d - 1
                    
                    better = False
                    if new_min < min_so_far[0]:
                        better = True
                    elif new_min == min_so_far[0]:
                        better = min_so_far[1] > new_dur
                        
                    if better:
                        min_so_far = [new_min, new_dur]
                dp[i] = min_so_far[:]
        return dp[-1][0]
                        
                    
            
        
        