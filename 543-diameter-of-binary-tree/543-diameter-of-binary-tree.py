# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        lp = 0
        stack = [[root, 0]]
        h = {}
        while stack:
            node, seen = stack[-1]
            if seen == 0:
                stack[-1][1] = 1
                if node.left:
                    stack.append([node.left, 0])
            elif seen == 1:
                stack[-1][1] = 2
                if node.right:
                    stack.append([node.right, 0])
            elif seen == 2:
                left = h.get(node.left, 0)
                right = h.get(node.right, 0)
                if left + right > lp:
                    lp = left + right
                h[node] = max(left, right) + 1
                stack.pop()
        return lp
        
                 
            