import heapq as hq
from random import randrange
class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_dist = [(x, y, x*x + y*y) for x,y in points]
        
        def recurse(check, start, end):
            idx = randrange(start, end + 1)
            x1, y1, dist1 = points_dist[idx][:]
            points_dist[idx], points_dist[end] = points_dist[end], points_dist[idx]
            starting = start
            for i in range(start, end):
                if points_dist[i][-1] <= dist1:
                    points_dist[i], points_dist[starting] = points_dist[starting], points_dist[i]
                    starting += 1
            points_dist[end], points_dist[starting] = points_dist[starting], points_dist[end]
            if starting == check - 1:
                return
            elif starting < check - 1:
                return recurse(check, starting + 1, end)
            return recurse(check, start, starting - 1)
        # def recurse(part, check):
        #     idx = randrange(0, len(part))
        #     x1, y1, dist1 = part[idx][:]
        #     left, right = [], []
        #     for i, point in enumerate(part):
        #         x, y, dist = point[:]
        #         if i == idx:
        #             continue
        #         elif dist <= dist1:
        #             left.append(point)
        #         else:
        #             right.append(point)
        #     if len(left) == check - 1:
        #         return (x1, y1, dist1)
        #     if len(left) < check - 1:
        #         return recurse(right, check - len(left) - 1)
        #     else:
        #         return recurse(left, check)
        # x_key, y_key, dist_key = recurse(points_dist, k)
        recurse(k, 0, len(points) - 1)
        return [points_dist[i][:-1] for i in range(k)]
        # ans = []
        # for point in points_dist:
        #     x,y,dist = point[:]
        #     if dist <= dist_key:
        #         ans.append([x, y])
        # return ans
        
        
        