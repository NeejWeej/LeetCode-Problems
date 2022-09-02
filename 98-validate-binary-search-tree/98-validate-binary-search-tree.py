# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(lb, up, node):
            if not node:
                return True
            
            if lb < node.val < up:
                left = isValid(lb, node.val, node.left)
                right = isValid(node.val, up, node.right)
                return left and right
            return False
        
        return isValid(float('-inf'), float('inf'), root)