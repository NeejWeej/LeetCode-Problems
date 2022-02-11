"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_ancestors = {}
        cur = p
        while cur:
            p_ancestors[cur.val] = cur
            cur = cur.parent
        while True:
            if q.val in p_ancestors:
                return p_ancestors[q.val]
            else:
                q = q.parent