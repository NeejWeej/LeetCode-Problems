class FreqStack:

    def __init__(self):
        self.freqs = {}
        self.freq_counts = collections.defaultdict(lambda: collections.deque([]))
        self.max = 0

    def push(self, val: int) -> None:
        self.freqs[val] = self.freqs.get(val, 0) + 1
        count = self.freqs[val]
        self.freq_counts[count].append(val)
        self.max = max(self.max, self.freqs.get(val))
        return
        
    def pop(self) -> int:
        ans = 0
        while not self.freq_counts[self.max]:
            self.max -= 1
        ans = self.freq_counts[self.max].pop()
        self.freqs[ans] = self.freqs.get(ans) - 1
        return ans

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()