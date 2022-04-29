# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        dummy = TreeNode()
        stack = [[dummy] + [0 for _ in range(5)],[root, 0, False, 0, 0]]
        while len(stack) > 1:
            cur, kidsSeen, is_left, left_height, right_height = stack[-1]
            if kidsSeen == 2:
                if abs(left_height - right_height) > 1:
                    return False
                height = max(left_height, right_height) + 1
                if is_left:
                    stack[-2][3] = height
                else:
                    stack[-2][4] = height
                stack.pop()
            elif kidsSeen == 0:
                stack[-1][1] = 1
                if cur.left:
                    stack.append([cur.left, 0, True, 0, 0])
            elif kidsSeen == 1:
                stack[-1][1] = 2
                if cur.right:
                    stack.append([cur.right, 0, False, 0, 0])
        return True  