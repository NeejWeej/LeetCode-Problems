class Solution:
    import heapq
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(vals, k):
            swap_idx = len(vals) - 1
            pivot = vals[-1]
            start = 0
            for i in range(len(vals) - 1):
                if vals[i] >= pivot:
                    vals[start], vals[i] = vals[i], vals[start]
                    start += 1
            vals[start], vals[swap_idx] = vals[swap_idx], vals[start]
            # print(vals, start)
            if start ==  k - 1:
                return vals[start]
            if start > k - 1:
                return quickSelect(vals[: start], k)
            return quickSelect(vals[start + 1:], k - start - 1)
        return quickSelect(nums, k)
    
    
        # k_large = [num for num in nums[:k]]
        # heapq.heapify(k_large)
        # for num in nums[k:]:
        #     if num > k_large[0]:
        #         heapq.heappushpop(k_large, num)
        # return k_large[0]
        