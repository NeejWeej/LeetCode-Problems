class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_large = [num for num in nums[:k]]
        heapq.heapify(k_large)
        for num in nums[k:]:
            if num >= k_large[0]:
                heapq.heappushpop(k_large, num)
        return k_large[0]
        