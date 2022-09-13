import heapq as hq
class MedianHeap:
    
    def __init__(self, isMax):
        self.max = isMax
        self.vals = []
        self.indices = set()
    
    def pop(self):
        while self.vals and self.vals[0][1] not in self.indices:
            hq.heappop(self.vals)
        res, idx = hq.heappop(self.vals)
        self.indices.remove(idx)
        return (res, idx) if self.max else (-res, idx)
    
    def push(self, val, idx):
        self.indices.add(idx)
        add = (val, idx) if self.max else (-val, idx)
        hq.heappush(self.vals, add)
    
    def remove(self, idx):
        if idx in self.indices:
            self.indices.remove(idx)
    
    def peek(self):
        while self.vals and self.vals[0][1] not in self.indices:
            hq.heappop(self.vals)
        res = self.vals[0][0]
        return res if self.max else -res
        
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        maxH = MedianHeap(True)
        minH = MedianHeap(False)
        
        n = len(nums)
        
        if k % 2:
            def median():
                return minH.peek()
        else:
            def median():
                return (maxH.peek() + minH.peek()) / 2
        
        for i in range(k - 1):
            val = nums[i]
            minH.push(val, i)
            maxH.push(*minH.pop())
            if len(maxH.vals) > len(minH.vals):
                minH.push(*maxH.pop())
        ans = []
        for i in range(k - 1, n):
            val = nums[i]
            minH.remove(i - k)
            maxH.remove(i - k)
            
            minH.push(val, i)
            maxH.push(*minH.pop())
            while len(maxH.indices) > len(minH.indices):
                minH.push(*maxH.pop())
            ans.append(median())
        
        return ans
            
        
            
            
            
            
        
        
            
        
        
        