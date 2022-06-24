# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def search(cur):
            if not cur:
                return -1
            left = 1 + search(cur.left)
            right = 1 + search(cur.right)
            self.ans = max(self.ans, left + right)
            return max(left, right)
        search(root)
        return self.ans