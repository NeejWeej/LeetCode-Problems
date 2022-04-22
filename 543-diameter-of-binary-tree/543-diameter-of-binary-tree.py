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
        heights = {}
        while stack:
            node, counter = stack[-1]
            if counter == 0:
                stack[-1][1] = 1
                if node.left:
                    stack.append([node.left, 0])
            elif counter == 1:
                stack[-1][1] = 2
                if node.right:
                    stack.append([node.right, 0])
            elif counter == 2:
                left = heights.get(node.left, 0)
                right = heights.get(node.right, 0)
                if left + right > lp:
                    lp = left + right
                heights[node] = max(left, right) + 1
                stack.pop()
        return lp
        
                 
            