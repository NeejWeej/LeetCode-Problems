class Solution:
    from collections import Counter, deque
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        counter_items = list(counts.items())
        deq = deque(counter_items)
        
        def getCombos(deq):
            if not deq:
                return [[]]
            k, count = deq.popleft()
            recurse = getCombos(deq)
            ans = []
            for i in range(count + 1):
                ans += [ [k]*i + r for r in recurse ]
            return ans
        
        return getCombos(deq)