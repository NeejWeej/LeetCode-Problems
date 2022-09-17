# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import random

class Solution:
    def randSide(self):
        return random.randint(1, 2)

    BOTH = 3
    LEFT = 2
    RIGHT = 1
    NONE = 0
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [[root, self.BOTH]]
        lca = -1
        seen_p = False
        seen_q = False
        while stack:
            idx = len(stack) - 1
            node, tag = stack[idx]
            if node.val == p.val: 
                seen_p = True
                if lca == -1:
                    lca = len(stack) - 1
                elif seen_q:
                    return stack[lca][0]
            if node.val == q.val:
                seen_q = True
                if lca == -1:
                    lca = len(stack) - 1
                elif seen_p:
                    return stack[lca][0]
                
            if tag == self.NONE:
                if lca == len(stack) - 1: 
                    lca -= 1
                    if lca == 0: return root
                stack.pop()
            
            elif tag == self.BOTH:
                rand = self.randSide()
                if tag - rand == self.LEFT:
                    if node.right: stack.append([node.right, self.BOTH])
                    stack[idx][1] = self.LEFT
                else:
                    if node.left: stack.append([node.left, self.BOTH])
                    stack[idx][1] = self.RIGHT
                
            else:
                if tag == self.LEFT:
                    if node.left: stack.append([node.left, self.BOTH])
                elif tag == self.RIGHT:
                    if node.right: stack.append([node.right, self.BOTH])
                stack[idx][1] = self.NONE

        
            
                