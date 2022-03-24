class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        smallest = largest = best = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            top3 = [num, num*smallest, num*largest]
            top3.sort()
            smallest = top3[0]
            largest = top3[-1]
            best = max(smallest, largest, best)
        return best