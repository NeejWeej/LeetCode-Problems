class Solution:
    import heapq
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        small = []
        heapq.heapify(nums)
        for i in range(4):
            small.append(heapq.heappop(nums))
        
        nums = [-x for x in nums]
        for val in small:
            nums.append(-val)
        heapq.heapify(nums)
        big = []
        for i in range(4):
            big.append(-heapq.heappop(nums))
        return min([x-y for x,y in zip(big, small[::-1])])
        
        
#         biggest = []
#         neg_nums = [-num for num in nums]
#         heapq.heapify(neg_nums)
#         for i in range(4):
#             biggest.append(-heapq.heappop(neg_nums))
#         smallest = []
#         heapq.heapify(nums)
#         for i in range(4):
#             smallest.append(heapq.heappop(nums)) 
#         # print(biggest, smallest)
#         return min([x - y for x,y in zip(biggest, smallest[::-1])])
        