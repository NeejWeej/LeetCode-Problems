class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque([(nums[0], 0)])
        for i in range(1, k):
            num = nums[i]
            while len(q) > 0 and num >= q[-1][0]:
                q.pop()
            q.append((num, i))
            
        ans = []
        idx = k
        while idx < len(nums):
            if q[0][1] + k < idx:
                q.popleft()
            ans.append(q[0][0])
            new_num = nums[idx]
            while len(q) > 0 and new_num >= q[-1][0]:
                q.pop()
            q.append((new_num, idx))
            idx += 1
        if q[0][1] + k < len(nums):
            q.popleft()
        ans.append(q[0][0])
        return ans
            