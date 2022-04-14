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
                  
        stack = [(root, 0)]
        path = []
        cur = root
        while stack:
            cur, h = stack.pop()
            while path and path[-1][-1] >= h:
                path.pop()
            path.append((cur, h))
            if cur.val == p.val or cur.val == q.val:
                break
            if cur.left:
                stack.append((cur.left, h + 1))
            if cur.right:
                stack.append((cur.right, h + 1))
            # print([x.val for x in stack], [x.val for x in path])
        # path = [x for x,y in path]
        node = q
        if path[-1][0].val == q.val:
            node = p
        idx = len(path) - 1
        if search(path[idx][0].left, node) or search(path[idx][0].right, node):
            return path[idx][0]
        idx -= 1
        while idx >= 0:
            if path[idx][0].left and path[idx][0].left.val != path[idx + 1][0].val:
                if search(path[idx][0].left, node):
                    return path[idx][0]
            elif path[idx][0].right and path[idx][0].right.val != path[idx + 1][0].val:
                if search(path[idx][0].right, node):
                    return path[idx][0]
            idx -= 1         
        
                    
        