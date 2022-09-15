# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(maxV, node):
            if not node:
                return
            
            if maxV <= node.val:
                self.ans += 1
            
            maxV = max(node.val, maxV)
            dfs(maxV, node.left)
            dfs(maxV, node.right)
        
        dfs(float('-inf'), root)
        return self.ans
                
            
            