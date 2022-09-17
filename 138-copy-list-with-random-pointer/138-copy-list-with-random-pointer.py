"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        nodeCreator = lambda: Node(0)
        
        mapping = collections.defaultdict(nodeCreator)
        
        cur = head
        
        while cur:
            image = mapping[cur]
            if cur.random:
                image.random = mapping[cur.random]
            image.val = cur.val
            if cur.next:
                image.next = mapping[cur.next]
            cur = cur.next  
        return mapping.get(head)
        