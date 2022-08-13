class Solution:
    import bisect
    import itertools
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        tickets = [1, 7, 30]
        costVals = list(map(tuple, zip(costs, [-1, -7, -30])))
        cost, duration = sorted(costVals, key= lambda x: x[0])[0]
        dpCosts = [float('inf') for _ in range(n)]
        dpDurations = [0 for _ in range(n)]
        dpCosts[0], dpDurations[0] = cost, -duration - 1
        for i,d in enumerate(itertools.islice(days, 1, n), 1):
            # we can extend day before without any worries
            if d - days[i - 1] <= dpDurations[i-1]:
                dpCosts[i] = dpCosts[i-1]
                dpDurations[i] = dpDurations[i-1] - (d - days[i-1])
            else:
                minCost, minDuration = float('inf'), 0
                for duration, price in zip(tickets, costs):
                    idx = bisect.bisect_left(days, d - duration + 1, lo=0, hi=i + 1)
                    prev = dpCosts[idx-1] if idx > 0 else 0
                    new_min = prev + price
                    new_dur = days[idx] + duration - d - 1
                    
                    better = (new_min < minCost) or (
                        new_min == minCost and minDuration > new_dur
                    )
                        
                    if better:
                        minCost, minDuration = new_min, new_dur
                dpCosts[i], dpDurations[i] = minCost, minDuration
        return dpCosts[-1]
                        
                    
            
        
        