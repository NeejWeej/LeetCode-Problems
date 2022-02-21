class Solution:
    import heapq, random
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if k >= n:
            return nums
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        final_freq = [[] for _ in range(n)]
        for num, count in counts.items():
            final_freq[count - 1].append(num)
        ans = []
        tally = 0
        for idx in range(n -1, -1, -1):
            these_counts = final_freq[idx]
            for val in these_counts:
                ans.append(val)
                tally += 1
                if tally == k:
                    return ans
            
        
        # counts = {}
        # for num in nums:
        #     counts[num] = counts.get(num, 0) + 1
        # count_items = []
        # for num, count in counts.items():
        #     heapq.heappush(count_items, (count, num))
        #     if len(count_items) > k:
        #         heapq.heappop(count_items)
        # return [x[1] for x in count_items]
        