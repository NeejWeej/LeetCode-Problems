# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def is_balanced_and_depth(self, root: Optional[TreeNode]) -> (bool, int):
        if root is None:
            return True, 0
        
        balanced_left, depth_left = self.is_balanced_and_depth(root.left)
        balanced_right, depth_right = self.is_balanced_and_depth(root.right)
        
        depth_difference = abs(depth_left - depth_right)
        both_balanced = balanced_left and balanced_right and depth_difference <= 1
        depth = max(depth_left, depth_right) + 1
        return both_balanced, depth
        
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced, _ = self.is_balanced_and_depth(root)
        return is_balanced