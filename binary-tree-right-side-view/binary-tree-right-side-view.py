# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    import collections
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        if not root:
            return []
        
        q = collections.deque([root])
        while q:
            ans.append(q[0].val)
            layer = collections.deque([])
            for _ in range(len(q)):
                cur = q.popleft()
                if cur.right:
                    layer.append(cur.right)
                if cur.left:
                    layer.append(cur.left)
            q = layer
    
        return ans