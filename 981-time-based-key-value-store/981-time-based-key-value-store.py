class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        key_tracker = self.keys.get(key, {})
        
        key_tracker[timestamp] = value
        
        times = key_tracker.get('TIMES', [])
        times.append(timestamp)
        key_tracker['TIMES'] = times
        self.keys[key] = key_tracker

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys:
            return ""
        key_vals = self.keys.get(key)
        times = key_vals.get('TIMES')
        lo = 0
        hi = len(times) - 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2
            mid_t = times[mid]
            if mid_t == timestamp:
                return key_vals[timestamp]
            elif timestamp < mid_t:
                hi = mid - 1
            else:   
                lo = mid
        if times[hi] <= timestamp:
            return key_vals[times[hi]]
        if times[lo] <= timestamp:
            return key_vals[times[lo]]
        return ""
            


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)