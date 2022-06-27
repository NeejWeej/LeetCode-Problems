class MyQueue:

    def __init__(self):
        self.forward = []
        self.rev = []

    def push(self, x: int) -> None:
        self.forward.append(x)

    def pop(self) -> int:
        if self.rev:
            return self.rev.pop()
        else:
            while self.forward:
                self.rev.append(self.forward.pop())
            return self.rev.pop()

    def peek(self) -> int:
        if self.rev:
            return self.rev[-1]
        else:
            while self.forward:
                self.rev.append(self.forward.pop())
            return self.rev[-1]

    def empty(self) -> bool:
        return len(self.forward) == len(self.rev) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()