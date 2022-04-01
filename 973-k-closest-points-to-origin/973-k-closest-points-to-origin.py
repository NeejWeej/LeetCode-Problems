import heapq as hq
from random import randrange
class Solution:
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points_dist = [(x, y, x*x + y*y) for x,y in points]
        
        def recurse(part, check):
            idx = randrange(0, len(part))
            x1, y1, dist1 = part[idx][:]
            left, right = [], []
            for i, point in enumerate(part):
                x, y, dist = point[:]
                if i == idx:
                    continue
                elif dist <= dist1:
                    left.append(point)
                else:
                    right.append(point)
            # print(left, right, check, (x1, y1))
            if len(left) == check - 1:
                return (x1, y1, dist1)
                # ans = [[x, y] for x,y,dist in left]
                # ans.append([x1, y1])
                # return ans
            if len(left) < check - 1:
                return recurse(right, check - len(left) - 1)
            else:
                return recurse(left, check)
        x_key, y_key, dist_key = recurse(points_dist, k)
        ans = []
        for point in points_dist:
            x,y,dist = point[:]
            if dist <= dist_key:
                ans.append([x, y])
        return ans
        
        
        