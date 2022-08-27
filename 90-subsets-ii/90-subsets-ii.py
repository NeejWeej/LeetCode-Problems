class Solution:
    from collections import Counter, deque
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        self.ans = set()
        counter_items = list(counts.items())
        n = len(counter_items)
        
        deq = deque(counter_items)
        
        def getCombos(deq):
            if not deq:
                return [[]]
            k, count = deq.popleft()
            recurse = getCombos(deq)
            ans = []
            for i in range(count + 1):
                ans += [ [i] + r for r in recurse ]
            return ans
        
        total = getCombos(deq)
        ans = []
        for group in total:
            new = []
            for i, val in enumerate(group):
                new += [counter_items[i][0]]* val
            ans.append(new)
        return ans