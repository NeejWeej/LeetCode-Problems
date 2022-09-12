class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        ans = []
        deq = collections.deque([])
        
        for i,n in enumerate(nums):
            while deq and deq[-1][0] <= n:
                deq.pop()
            deq.append([n, i])
            if i - k >= deq[0][1]:
                deq.popleft()
            if i >= k - 1:
                ans.append(deq[0][0])
            
        return ans
        