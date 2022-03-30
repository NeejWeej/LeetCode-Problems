class MyQueue:

    def __init__(self):
        self.in_order = []
        self.reversed = []

    def push(self, x: int) -> None:
        self.in_order.append(x)
    
    def switch(self):
        while self.in_order:
            remove = self.in_order.pop()
            self.reversed.append(remove)

    def pop(self) -> int:
        if not self.reversed:
            self.switch()
        return self.reversed.pop()

    def peek(self) -> int:
        if not self.reversed:
            self.switch()
        return self.reversed[-1]

    def empty(self) -> bool:
        return not self.in_order and not self.reversed


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()