from collections import defaultdict

class PathTimeInfo:
    def __init__(self):
        self.totalTime = 0
        self.totalCount = 0

class UndergroundSystem:

    def __init__(self):
        self.customers = {}
        self.paths = defaultdict(PathTimeInfo)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customers[id] = (t, stationName)
        
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        enterTime, oldStation = self.customers.pop(id)
        stationPath = (oldStation, stationName)
        pathInfo = self.paths[stationPath]
        pathInfo.totalTime += (t - enterTime)
        pathInfo.totalCount += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        path = (startStation, endStation)
        pathInfo = self.paths[path]
        return pathInfo.totalTime / pathInfo.totalCount
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)