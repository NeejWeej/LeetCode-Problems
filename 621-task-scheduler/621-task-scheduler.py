from collections import Counter, defaultdict
import heapq as hq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        counter = Counter(tasks)
        top = counter.most_common(1)[0]
        best = top[1]
        best_count = 0
        for k,v in counter.items():
            if v == best:
                best_count += 1
        return max(len(tasks), best_count + (n + 1)*(best - 1))
            