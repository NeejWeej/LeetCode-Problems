# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # from collections import deque
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return root
        stack = [root]
        ans = []
        while stack:
            new_layer = []
            cur_level = []
            for node in stack:
                cur_level.append(node.val)
                if node.left:
                    new_layer.append(node.left)
                if node.right:
                    new_layer.append(node.right)
            ans.append(cur_level)
            stack = new_layer
        return ans