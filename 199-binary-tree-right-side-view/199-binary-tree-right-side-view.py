# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        stack = [root]
        ans = []
        while stack:
            nextStack = []
            ans.append(stack[-1].val)
            for n in stack:
                if n.left:
                    nextStack.append(n.left)
                if n.right:
                    nextStack.append(n.right)
            stack = nextStack
        return ans
                
        