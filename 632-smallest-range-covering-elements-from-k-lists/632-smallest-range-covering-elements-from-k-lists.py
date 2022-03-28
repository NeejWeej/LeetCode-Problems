import heapq as hq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # cur = [x[0] for x in nums]
        n = len(nums)
        cur = [0 for _ in range(n)]
        cur_heap = [(nums[x][0], x) for x in range(n)]
        hq.heapify(cur_heap)
        # cur_vals = [x[0] for x in nums]
        
        finished_min = float('inf')
        finished_max = float('-inf')
        # hq.heapify(cur_vals)
        
        
        cur_max = max(cur_heap)[0]
        best = [cur_heap[0][0], cur_max]
        while cur_heap:
            val, list_from = hq.heappop(cur_heap)[:]
            if cur[list_from] < len(nums[list_from]) - 1:
                cur[list_from] += 1
                new_idx = cur[list_from]
                new_val = nums[list_from][new_idx]
                # cur_vals[list_from] = new_val
                if new_val > cur_max:
                    cur_max = new_val
                hq.heappush(cur_heap, (new_val, list_from))
                cur_min = min(finished_min, cur_heap[0][0])
                cur_range = [cur_min, max(cur_max, finished_max)]
                # print(cur_range, cur_vals)
                if cur_range[1] - cur_range[0] < best[1] - best[0]:
                    best = cur_range
            else:
                if val < finished_min:
                    finished_min = val
                if val > finished_max:
                    finished_max = val
        return best
            
            
        
        
        
        