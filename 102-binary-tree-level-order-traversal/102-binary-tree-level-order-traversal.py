# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root]
        ans = []
        while q:
            ans.append([x.val for x in q])
            newl = []
            for node in q:
                if node.left:
                    newl.append(node.left)
                if node.right:
                    newl.append(node.right)
            q = newl
        return ans