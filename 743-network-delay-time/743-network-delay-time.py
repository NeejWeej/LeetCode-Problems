from collections import defaultdict
import heapq as hq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(dict)
        for u, s, w in times:
            graph[u][s] = w
        
        d = [(time, s) for s,time in graph.get(k, {}).items()]
        hq.heapify(d)
        lastTime = 0
        seen =set([k])
        while d and len(seen) < n:
            time, nextNode = hq.heappop(d)
            if nextNode not in seen:
                lastTime = time
                seen.add(nextNode)
                for child, delay in graph.get(nextNode, {}).items():
                    if child not in seen:
                        hq.heappush(d, (time + delay, child))
                    
        return lastTime if len(seen) == n else -1
        