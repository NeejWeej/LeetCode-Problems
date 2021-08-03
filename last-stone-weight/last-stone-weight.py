class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        neg_stones = [-x for x in stones]
        heapq.heapify(neg_stones)
        heap = neg_stones
        while len(heap)>1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            if x == y:
                continue
            heapq.heappush(heap,x-y)
        if heap:
            return -heap[0]
        return 0