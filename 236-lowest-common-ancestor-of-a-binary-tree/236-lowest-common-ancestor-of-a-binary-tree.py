# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def isEqual(path, curNode, target):
            path.append(curNode)
            if curNode.val == target:
                return path
            left = None
            if curNode.left:
                left = isEqual(path, curNode.left, target)
            if left: return left
            right = None
            if curNode.right:
                right = isEqual(path, curNode.right, target)
            if right: return right
            path.pop()
            return None
        
        
        p_path = isEqual([], root, p.val)
        p_set = set(p_path)
        q_path = isEqual([], root, q.val)
        for n in reversed(q_path):
            if n in p_path:
                return n
            