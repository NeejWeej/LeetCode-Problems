# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(r, p1, q1):
            if p1 <= r.val and r.val <= q1:
                return r
            if p1 >= r.val:
                return lca(r.right, p1, q1)
            return lca(r.left, p1, q1)
        
        if p.val > q.val:
            p, q = q, p
        return lca(root, p.val, q.val)