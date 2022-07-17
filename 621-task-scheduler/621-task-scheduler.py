from collections import Counter
import heapq as hq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        counts = Counter(tasks)
        avail = [(-v, 0, k) for k,v in counts.items()]
        hq.heapify(avail)
        time = 0
        heap = []
        while heap or avail:
            # print(avail)
            # print(heap)
            # print('~'*10)
            while heap and heap[0][0] <= time:
                nextTime, count, key = hq.heappop(heap)
                hq.heappush(avail, (count, nextTime, key))
            nextTime = count = key = None
            if avail:
                count, nextTime, key = hq.heappop(avail)
            else:
                nextTime, count, key = hq.heappop(heap)
            count += 1
            time = max(nextTime + 1, time + 1)
            if count < 0:
                hq.heappush(heap, (time + n, count, key))
        return time
            