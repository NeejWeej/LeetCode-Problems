class Solution:
    import random
    def __init__(self, w: List[int]):
        cur_sum = 0
        self.prefix_sum = []
        for val in w:
            cur_sum += val
            self.prefix_sum.append(cur_sum)
        self.tot = cur_sum  
    def pickIndex(self) -> int:
        in_prefix = random.randrange(1, self.tot + 1)
        start = 0
        end = len(self.prefix_sum)
        while start < end:
            mid = start + (end - start) // 2
            if in_prefix == self.prefix_sum[mid]:
                return mid
            elif in_prefix < self.prefix_sum[mid]:
                end = mid
            elif in_prefix > self.prefix_sum[mid]:
                start = mid + 1
        return start
        # if start == end:
        #     return start
        # if start + 1 == end:
        #     if in_prefix <= self.prefix_sum[start]:
        #         return start
        #     return end
        
        
            


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()