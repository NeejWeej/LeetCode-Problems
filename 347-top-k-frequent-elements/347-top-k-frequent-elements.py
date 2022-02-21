class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) - 1
        count_items = [(neg_count, val) for val, neg_count in counts.items()]
        heapq.heapify(count_items)
        ans = []
        for i in range(k):
            popped = heapq.heappop(count_items)
            ans.append(popped[1])
        return ans
        