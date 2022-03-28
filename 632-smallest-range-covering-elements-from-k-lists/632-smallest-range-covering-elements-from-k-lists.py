import heapq as hq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # cur = [x[0] for x in nums]
        n = len(nums)
        cur = [0 for _ in range(n)]
        cur_heap = [(nums[x][0], x) for x in range(n)]
        hq.heapify(cur_heap)
        cur_vals = [x[0] for x in nums]
        cur_max = max(cur_vals)
        best = [min(cur_vals), cur_max]
        while cur_heap:
            val, list_from = hq.heappop(cur_heap)[:]
            if cur[list_from] == len(nums[list_from]) - 1:
                continue
            else:
                cur[list_from] += 1
                new_idx = cur[list_from]
                new_val = nums[list_from][new_idx]
                cur_vals[list_from] = new_val
                if new_val > cur_max:
                    cur_max = new_val
                cur_range = [min(cur_vals), cur_max]
                # print(cur_range, cur_vals)
                hq.heappush(cur_heap, (new_val, list_from))
                if cur_range[1] - cur_range[0] < best[1] - best[0]:
                    best = cur_range
        return best
            
            
        
        
        
        