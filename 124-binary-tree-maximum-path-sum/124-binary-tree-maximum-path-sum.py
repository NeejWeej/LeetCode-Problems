# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mps(self, root):
        left, right = 0, 0
        if root.left:
            left = max(0, self.mps(root.left))
        if root.right:
            right = max(0, self.mps(root.right))
        self.best = max(self.best, root.val + left + right)
        return root.val + max(left, right)
        
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.best = root.val
        self.mps(root)
        return self.best
        