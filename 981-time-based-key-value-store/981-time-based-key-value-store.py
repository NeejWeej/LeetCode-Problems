from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        times = self.keys.get(key)
        if not times:
            return ""
        lo = 0
        hi = len(times) - 1
        while lo + 1< hi:
            mid = lo + (hi - lo) // 2
            mid_t = times[mid]
            if mid_t[0] == timestamp:
                return mid_t[1]
            elif timestamp < mid_t[0]:
                hi = mid - 1
            else:   
                lo = mid
        if times[hi][0] <= timestamp:
            return times[hi][1]
        if times[lo][0] <= timestamp:
            return times[lo][1]
        return ""
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)