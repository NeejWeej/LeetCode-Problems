# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getHeight(self, root):
        if not root:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        if left + right > self.longest_path:
            self.longest_path = left + right
        return max(left, right) + 1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.longest_path = 0
        self.getHeight(root)
        return self.longest_path
            