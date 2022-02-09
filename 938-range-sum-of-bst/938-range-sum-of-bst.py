# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, low, high):
        lower_bound = low <= root.val
        upper_bound = root.val <= high
        if lower_bound and upper_bound:
            self.ans += root.val
        if upper_bound and root.right:
            self.dfs(root.right, low, high)
        if lower_bound and root.left:
            self.dfs(root.left, low, high)
        return
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.ans = 0
        self.dfs(root, low, high)
        return self.ans