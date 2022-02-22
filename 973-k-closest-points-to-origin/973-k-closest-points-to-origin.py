class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        new_tups = [(x*x + y*y, x, y) for x,y in points]
        heapq.heapify(new_tups)
        ans = []
        for _ in range(k):
            new_closest = heapq.heappop(new_tups)
            dist, x, y = new_closest[:]
            ans.append([x,y])
        return ans
        