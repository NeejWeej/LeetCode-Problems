class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        ans = []
        counts = [(-count,key) for key,count in counter.items()]
        heapq.heapify(counts)
        
        for _ in range(k):
            count, key = heapq.heappop(counts)
            ans.append(key)
        return ans
            
            
            
        
        