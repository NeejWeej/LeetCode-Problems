class Node:
    def __init__(self, value, time = float('inf')):
        self.val = value
        self.time = time
    
    def __lt__(self, other):
        return self.time < other.time
        

class Solution:
    import heapq
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set([k])
        
        connections = collections.defaultdict(list)
        for source, target, time in times:
            connections[source].append((target, time))
            
        nodes = {x: Node(x) for x in range(1, n + 1)}

        max_time = 0
        nodes.get(k).time = 0
        
        pq = [nodes.get(k)]
        
        while pq:
            cur = heapq.heappop(pq)
            visited.add(cur.val)
            
            if cur.time > max_time:
                max_time = cur.time
            
            for target, time in connections.get(cur.val, []):
                if target not in visited:
                    target_time = nodes.get(target).time
                    if target_time == float('inf'):
                        pq.append(nodes.get(target))
                        # heapq.heappush(pq, nodes.get(target))     
                    nodes.get(target).time = min(target_time, cur.time + time)
            
            heapq.heapify(pq)
        return max_time if len(visited) == n else -1
        