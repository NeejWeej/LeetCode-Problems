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
        clone_dict = {node.val: Node(node.val)}
        seen = set([node.val])
        stack = [node]
        while stack:
            cur = stack.pop()
            cur_copy = clone_dict.get(cur.val)
            for neigh in cur.neighbors:
                if neigh.val not in clone_dict:
                    clone_dict[neigh.val] = Node(neigh.val)
                neigh_copy = clone_dict.get(neigh.val)
                
                cur_copy.neighbors.append(neigh_copy)
                
                if neigh.val not in seen:
                    stack.append(neigh)
                    seen.add(neigh.val)
        return clone_dict.get(node.val)
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#                 if not node: return None
#         clones = collections.defaultdict(lambda : Node())
#         stack = [node]
#         visited = set([node.val])
#         while stack:
#             curr = stack.pop()
#             cVal = curr.val
#             clones[cVal].val = cVal
#             for neighbor in curr.neighbors:
#                 nVal = neighbor.val
#                 clones[cVal].neighbors.append(clones[nVal])
#                 if nVal not in visited:
#                     stack.append(neighbor)
#                     visited.add(nVal)
#         return clones.get(node.val)