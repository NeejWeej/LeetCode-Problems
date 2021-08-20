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
            if curr in visited:
                continue
            visited.add(curr)
            clones[curr].val = curr.val
            for neighbor in curr.neighbors:
                clones[curr].neighbors.append(clones[neighbor])
                stack.append(neighbor)
        return clones.get(node)
        