# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isEqual(node, other):
            if not node or not other:
                return not node and not other
            return node.val == other.val and isEqual(node.left, other.left) and isEqual(node.right, other.right)
        
        
        def recSubtree(cur, goal):
            if cur == goal:
                return True
            
            if not cur or not goal:
                return not cur and not goal
            
            if isEqual(cur, goal):
                return True
            
            return recSubtree(cur.left, goal) or recSubtree(cur.right, goal)
        
        return recSubtree(root, subRoot)
        