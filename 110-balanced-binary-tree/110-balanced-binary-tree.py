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
        stack = [[root] + [0 for _ in range(5)],[root, 0, False, 0, 0]]
        while len(stack) > 1:
            cur, kidsSeen, is_left, left, right = stack[-1]
            if kidsSeen == 2:
                if abs(left - right) > 1:
                    return False
                if is_left:
                    stack[-2][3] = max(left, right) + 1
                else:
                    stack[-2][4] = max(left, right) + 1
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