class Solution:
    import heapq
    from random import randrange
    def findKthLargest(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        spot = k
        while l <= r:
            swap_idx = r
            pivot = nums[swap_idx]
            start = l
            # print(pivot)
            for i in range(l, r):
                if nums[i] >= pivot:
                    nums[start], nums[i] = nums[i], nums[start]
                    start += 1
                    
            nums[start], nums[r] = nums[r], nums[start]
            # print(nums, l, r, spot, start)
            if start == spot - 1:
                return nums[start]
            
            elif start > spot - 1:
                r = start - 1
                
            elif start < spot - 1:
                l = start + 1
                # we comment out the line below since we dont reset the spot
                # spot -= l
        
#         def quickSelect(vals, k):
#             swap_idx = len(vals) - 1
            
#             pivot = vals[swap_idx]
#             start = 0
#             for i in range(len(vals)):
#                 if i == swap_idx:
#                     continue
#                 if vals[i] >= pivot:
#                     vals[start], vals[i] = vals[i], vals[start]
#                     start += 1
#             vals[start], vals[swap_idx] = vals[swap_idx], vals[start]
#             # print(vals, pivot, start)
#             if start ==  k - 1:
#                 return vals[start]
#             if start > k - 1:
#                 return quickSelect(vals[: start], k)
#             return quickSelect(vals[start + 1:], k - start - 1)
#         return quickSelect(nums, k)
    
    
        # k_large = [num for num in nums[:k]]
        # heapq.heapify(k_large)
        # for num in nums[k:]:
        #     if num > k_large[0]:
        #         heapq.heappushpop(k_large, num)
        # return k_large[0]
        