"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    import collections
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        q = collections.deque([])
        q.append((root, 1))

        depth = 1
        while q:
            cur, depth = q.popleft()
            for child in cur.children:
                q.append((child, depth + 1))
        
        return depth
            
            
        