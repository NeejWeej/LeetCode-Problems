"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        clones = collections.defaultdict(lambda : Node())
        stack = [node]
        visited = set()
        while stack:
            curr = stack.pop()
            visited.add(curr.val)
            clones[curr].val = curr.val
            for neighbor in curr.neighbors:
                clones[curr].neighbors.append(clones[neighbor])
                if neighbor.val not in visited:
                    stack.append(neighbor)
                    visited.add(neighbor.val)
        return clones.get(node)
        