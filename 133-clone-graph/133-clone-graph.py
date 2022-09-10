"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        cloneG = collections.defaultdict(Node)
        if not node:
            return
        def addGraph(g, n, seen):
            if n.val in seen:
                return
            seen.add(n.val)
            g[n.val].val = n.val
            for neigh in n.neighbors:
                g[n.val].neighbors.append(g[neigh.val])
                if neigh.val not in seen:
                    addGraph(g, neigh, seen)
            
        addGraph(cloneG, node, set())
        return cloneG[node.val]
        
        
        