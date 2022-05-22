import heapq as hq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        chars = Counter(tasks)
        hqq = [(-count, char) for char,count in chars.items()]
        hq.heapify(hqq)
        time = 0
        dq = deque([])
        # print(hqq)
        while hqq or dq:
            # print(hqq, dq, time)
            time_s = float('inf')
            if dq:
                time_s, ch, count = dq[0]
            if not hqq:
                dq.popleft()
                count += 1
                time = time_s + 1
                if count < 0:
                    dq.append((time + n, ch, count))
            else:
                if time_s <= time:
                    dq.popleft()
                    hq.heappush(hqq, (count, ch))
                count, ch = hq.heappop(hqq)
                time += 1
                count += 1
                if count < 0:
                    dq.append((time + n, ch, count))
        return time
        
            
        