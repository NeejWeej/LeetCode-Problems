from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        vals = self.d.get(key, [])
        left, right = 0, len(vals)
        if not vals or vals[0][0] > timestamp:
            return ""
        
        while left < right:
            mid = (left + right)//2
            if vals[mid][0] <= timestamp:
                left = mid + 1  
            else:
                right = mid
        return vals[left - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)