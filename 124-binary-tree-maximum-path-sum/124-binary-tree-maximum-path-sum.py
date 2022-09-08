# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')
        
        def recurse(node):
            if not node:
                return 0
            left = max(0, recurse(node.left))
            right = max(0, recurse(node.right))
            self.ans = max(left + right + node.val, self.ans)
            return node.val + max(left, right)
        recurse(root)
        return self.ans