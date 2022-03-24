import heapq as hq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.max = []

    def addNum(self, num: int) -> None:
        if len(self.min) == len(self.max):
            to_min = hq.heappushpop(self.max, num)
            hq.heappush(self.min, -to_min)
        else:
            to_max = hq.heappushpop(self.min, -num)
            hq.heappush(self.max, -to_max)

    def findMedian(self) -> float:
        if len(self.min) == len(self.max):
            return (self.max[0] - self.min[0]) / 2
        else:
            return -self.min[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()