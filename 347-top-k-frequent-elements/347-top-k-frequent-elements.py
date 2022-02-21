class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        count_items = []
        for num, count in counts.items():
            heapq.heappush(count_items, (count, num))
            if len(count_items) > k:
                heapq.heappop(count_items)
        return [x[1] for x in count_items]
        