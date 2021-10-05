class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.size = capacity

    def get(self, key: int) -> int:
        if key in self.dict:
            res = self.dict.pop(key)
            self.dict[key] = res
            return res
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            res = self.dict.pop(key)
            self.dict[key] = value
            return
        else:
            if len(self.dict) == self.size:
                k = next(iter(self.dict.keys()))
                del self.dict[k]
            self.dict[key] = value
            return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)