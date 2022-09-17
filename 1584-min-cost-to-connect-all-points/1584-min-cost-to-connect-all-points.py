class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cost = 0
        n = len(points)
        if n <= 1:
            return 0
        
        included = set()
        
        distances = []
        
        nodeToDist = collections.defaultdict(list)
        
        for i, p in enumerate(points):
            tupP = tuple(p)
            for j in range(i + 1, n):
                otherP = tuple(points[j])
                dist = abs(p[0] - otherP[0]) + abs(p[1] - otherP[1]) 
                nodeToDist[tupP].append((dist, otherP))
                nodeToDist[otherP].append((dist, tupP))
        
        
        distances = nodeToDist[tuple(points[0])]
        heapq.heapify(distances)
        included.add(tuple(points[0]))
        
        while len(included) < n:
            d, p1 = heapq.heappop(distances)
            if p1 not in included:
                cost += d
                included.add(p1)
                for pair in nodeToDist.get(p1):
                    if pair not in included:
                        heapq.heappush(distances, pair)
                    
        return cost
                