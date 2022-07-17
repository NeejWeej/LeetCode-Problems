from collections import Counter, defaultdict
import heapq as hq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        counter = defaultdict(int)
        best = 0
        for t in tasks:
            counter[t] += 1
            if counter[t] > best:
                best = counter[t]
        best_count = 0
        for k,v in counter.items():
            if v == best:
                best_count += 1
        return max(len(tasks), best_count + (n + 1)*(best - 1))
            