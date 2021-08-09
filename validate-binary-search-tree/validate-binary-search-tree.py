# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValid(self, root):
        # returns [isBST, min, max]
        if not root:
            return [True, float('inf'), float('-inf')]
        left_side = self.isValid(root.left)
        right_side = self.isValid(root.right)
        if left_side[0] and right_side[0]:
            if root.val > left_side[2] and root.val < right_side[1]:
                new_min = min(root.val, left_side[1], right_side[1])
                new_max = max(root.val, left_side[2], right_side[2])
                return [True, new_min, new_max]
        return [False, float('inf'), float('-inf')]
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root)[0]
        