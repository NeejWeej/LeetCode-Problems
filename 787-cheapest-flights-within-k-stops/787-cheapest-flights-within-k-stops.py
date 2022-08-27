class Solution:
    from collections import defaultdict
    import heapq as hq
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #Bellman Ford let's do it
        
        inf = float('inf')
        graph = defaultdict(dict)
        for from_, to_, p in flights:
            graph[from_][to_] = p
        
        costs = [inf]*n
        costs[src] = 0
        
        q = [src]
        steps = 0
        
        while q and steps < k + 1:
            steps += 1
            nq = []
            newCosts = list(costs)
            
            for city in q:
                cost = costs[city]
                leavingCity = graph.get(city, {})
                for to_, p in leavingCity.items():
                    if newCosts[to_] > cost + p:
                        newCosts[to_] = cost + p
                        nq.append(to_)
            q = nq
            costs = newCosts
            
        return costs[dst] if costs[dst] != inf else -1
                    
            
        
        