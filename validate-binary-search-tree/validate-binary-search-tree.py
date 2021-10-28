# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    import collections
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        q = collections.deque([(root, float('-inf'), float('inf'))])
        while q:
            cur, low_b, up_b = q.popleft()
            if cur.val <= low_b or up_b <= cur.val:
                return False
            if cur.left:
                new_left = (cur.left, low_b, cur.val)
                q.append(new_left)
            if cur.right:
                new_right = (cur.right, cur.val, up_b)
                q.append(new_right)
        return True
        
                
        