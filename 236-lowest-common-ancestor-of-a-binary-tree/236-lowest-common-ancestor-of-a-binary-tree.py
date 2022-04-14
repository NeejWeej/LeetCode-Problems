# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def search(start, node):
            if not start:
                return False
            stack = [start]
            while stack:
                cur = stack.pop()
                if cur.val == node.val:
                    return True
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
            return False
                  
        stack = [root]
        path = []
        cur = root
        found_p_q = False
        while stack:
            cur = stack.pop()
            path.append(cur)
            if cur.val == p.val or cur.val == q.val:
                break
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
            if not cur.left and not cur.right:
                path.pop()
        if path[-1].val == p.val:
            idx = len(path) - 1
            if search(path[idx].left,q) or search(path[idx].right, q):
                return path[idx]
            idx -= 1
            while idx >= 0:
                if path[idx].left and path[idx].left.val != path[idx + 1].val:
                    if search(path[idx].left, q):
                        return path[idx]
                elif search(path[idx].right, q):
                    return path[idx]
                idx -= 1
        elif path[-1].val == q.val:
            idx = len(path) - 1
            if search(path[idx].left, p) or search(path[idx].right, p):
                return path[idx]
            idx -= 1
            # print([x.val for x in path], idx)
            while idx >= 0:
                if path[idx].left and path[idx].left.val != path[idx + 1].val:
                    if search(path[idx].left, p):
                        return path[idx]
                elif search(path[idx].right, p):
                    return path[idx]
                idx -= 1            
        
                    
        