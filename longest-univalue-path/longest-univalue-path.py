# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.ans = 0
        def best_path(x):
            if not x.left and not x.right:
                return (x.val, 0)
            
            best_left = (float('inf'), 0)
            if x.left:
                best_left = best_path(x.left)
            
            best_right = (float('inf'),0)
            if x.right:
                best_right = best_path(x.right)
            
            if best_left[0] != x.val and best_right[0] != x.val:
                return (x.val, 0)
            
            if best_left[0] == x.val and best_right[0] != x.val:
                new_pos = best_left[1] + 1
                self.ans = max(self.ans, new_pos)
                return (x.val, new_pos)
  
            if best_left[0] != x.val and best_right[0] == x.val:
                new_pos = best_right[1] + 1
                self.ans = max(self.ans, new_pos)
                return (x.val, new_pos)
            
            else:
                self.ans = max(self.ans, best_left[1] + best_right[1] + 2)
                return (x.val, max(best_left[1], best_right[1]) + 1)  
        best_path(root)
        return self.ans
        