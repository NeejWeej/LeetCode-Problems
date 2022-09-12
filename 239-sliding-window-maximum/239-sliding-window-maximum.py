class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        deq = collections.deque([])
        
        def adjustDeq(deq, nums, idx):
            n = nums[idx]
            while deq and deq[-1][0] <= n:
                deq.pop()
            deq.append([n, idx])
            
        for i in range(k - 1):
            adjustDeq(deq, nums, i)
        
        for i in range(k - 1, len(nums)):
            adjustDeq(deq, nums, i)
            
            if i - k >= deq[0][1]:
                deq.popleft()
            ans.append(deq[0][0])
            
        return ans
        