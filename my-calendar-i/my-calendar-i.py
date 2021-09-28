class Node:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None
    
    def insert(self, node):
        if self.start >= node.end:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
            
        elif self.end <= node.start:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        
        return False


class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        new_Node = Node(start, end)
        if not self.root:
            self.root = new_Node
            return True
        return self.root.insert(new_Node)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)