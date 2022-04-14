# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        stack = [[root, 0]]
        while stack:
            cur, seen_left = stack[-1]
            if seen_left == 0:
                stack[-1][1] = 1
                if cur.left:
                    stack.append([cur.left, 0])
            elif seen_left == 1:
                count += 1
                if count == k:
                    return cur.val
                stack.pop()
                if cur.right:
                    stack.append([cur.right, 0])
                