import heapq as hq

class MedianFinder:

    def __init__(self):
        self.smallerHalf = []
        self.largerHalf = []

    def addNum(self, num: int) -> None:
        hq.heappush(self.smallerHalf, -num)
        hq.heappush(self.largerHalf, -hq.heappop(self.smallerHalf))
        if len(self.smallerHalf) < len(self.largerHalf):
            hq.heappush(self.smallerHalf, -hq.heappop(self.largerHalf))

    def findMedian(self) -> float:
        if len(self.smallerHalf) == len(self.largerHalf):
            # subtract since smallerHalf stores negative numbers
            return (self.largerHalf[0] - self.smallerHalf[0]) / 2
        else:
            return -self.smallerHalf[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()