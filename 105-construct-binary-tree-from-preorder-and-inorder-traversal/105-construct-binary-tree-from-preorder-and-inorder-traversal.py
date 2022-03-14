# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        start = TreeNode(preorder[0])
        if len(preorder) == 1:
            return start
        inorder_idx = 0
        while inorder[inorder_idx] != preorder[0]:
            inorder_idx += 1
        left_inorder = inorder[:inorder_idx]
        left_preorder = preorder[1: inorder_idx + 1]
        left = self.buildTree(left_preorder, left_inorder)
        right = self.buildTree(preorder[inorder_idx + 1:], inorder[inorder_idx + 1:])
        start.left = left
        start.right = right
        return start