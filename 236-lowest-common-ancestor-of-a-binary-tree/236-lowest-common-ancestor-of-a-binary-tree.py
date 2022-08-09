# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    BOTH = 2
    RIGHT = 1
    DONE = 0
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [[root, self.BOTH]]
        lca = -1
        seen_p = False
        seen_q = False
        while stack:
            node, tag = stack[-1]
            if node.val == p.val: 
                seen_p = True
            if node.val == q.val:
                seen_q = True
            if seen_q and seen_p:
                return stack[lca][0]
            if (seen_q or seen_p) and lca == -1:
                lca = len(stack) - 1
            if tag == self.BOTH:
                stack[-1][1] = tag - 1
                if node.left: stack.append([node.left, self.BOTH])
            elif tag == self.RIGHT:
                stack[-1][1] = tag - 1
                if node.right: stack.append([node.right, self.BOTH])
            elif tag == self.DONE:
                if lca == len(stack) - 1: lca -= 1
                stack.pop()
        
            
                