class Solution:
    import heapq
    
    def dist(self, p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        list_of_points = {}
        for p1 in range(n):
            for p2 in range(p1 + 1, n):
                if p1 in list_of_points:
                    list_of_points[p1].append((self.dist(points[p1],points[p2]), p2, p1))
                else:
                    list_of_points[p1] = [(self.dist(points[p1],points[p2]), p2, p1)]
                
                if p2 in list_of_points:
                    list_of_points[p2].append((self.dist(points[p1],points[p2]), p1, p2))
                else:
                    list_of_points[p2] = [(self.dist(points[p1],points[p2]), p1, p2)]
            heapq.heapify(list_of_points.get(p1))
        visited = set([0])
        pq = list_of_points.get(0)
        total = 0
        while pq:
            cur_edge = heapq.heappop(pq)
            dist, dest, start = cur_edge[:]
            if dest not in visited:
                total += dist
                visited.add(dest)
                if list_of_points.get(dest):
                    to_add = heapq.heappop(list_of_points.get(dest))
                    heapq.heappush(pq, to_add)
                if list_of_points.get(start):
                    to_add2 = heapq.heappop(list_of_points.get(start))
                    heapq.heappush(pq, to_add2)
            else:
                if list_of_points.get(start):
                    to_add2 = heapq.heappop(list_of_points.get(start))
                    heapq.heappush(pq, to_add2)                
                # heapq.heappush(pq, to_add)
                # pq += [x for x in list_of_points.get(dest) if x[1] not in visited]
                # heapq.heapify(pq)
        return total
#         edges = [
#             (self.dist(points[p1],points[p2]), tuple(points[p1]), tuple(points[p2]))
#             for p1 in range(n) for p2 in range(n)
#         ]
        
#         heapq.heapify(edges)
#         total = 0
#         visited = set()
        
#         while len(edges) > 0:
#             cur_edge = heapq.heappop(edges)
#             dist, p1, p2 = cur_edge[:]
#             # print(dist, p1, p2)
#             if dist == 0:
#                 continue
#             if p1 not in visited or p2 not in visited:
#                 # print(dist, total, p1, p2)
#                 visited.add(p1)
#                 visited.add(p2)
#                 total += dist       
#             if len(visited) == n:
#                 return total
                
#         return total