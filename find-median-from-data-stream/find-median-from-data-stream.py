class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_h = []
        self.max_h = []

    def addNum(self, num: int) -> None:
        #add to max one
        #pop smallest
        #put that one in the small one
        #if small one greater than largest by more than 1
        #add that new one to the large one
        from_big = heapq.heappushpop(self.max_h, num)
        heapq.heappush(self.min_h, -from_big)
        if len(self.min_h) > len(self.max_h) + 1:
            from_small = heapq.heappop(self.min_h)
            heapq.heappush(self.max_h, -from_small)
        return

    def findMedian(self) -> float:
        if not self.min_h:
            return self.max_h[0]
        elif not self.max_h:
            return -self.min_h[0]
        elif len(self.min_h) == len(self.max_h):
            return (-self.min_h[0] + self.max_h[0])/2
        elif len(self.min_h) == len(self.max_h) + 1:
            return -self.min_h[0]
        return self.max_h[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()