# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, low, high):
        if low <= root.val and root.val <= high:
            self.ans += root.val
        if root.val <= high and root.right:
            self.dfs(root.right, low, high)
        if root.val >= low and root.left:
            self.dfs(root.left, low, high)
        return
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        self.dfs(root, low, high)
        return self.ans