# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
        
    def contains_p_q(self, node, p, q):
        ans = [False, False]
        if node.val == p.val:
            ans[0] = True
        elif node.val == q.val:
            ans[1] = True
        right = [False, False]
        left = [False, False]
        if node.right:
            right = self.contains_p_q(node.right, p, q)
        if node.left:
            left = self.contains_p_q(node.left, p, q)
        ans[0] = ans[0] or right[0] or left[0]
        ans[1] = ans[1] or right[1] or left[1]
        if not(ans[0] and ans[1]):
            return [ans[0], ans[1], None]
        if not(right[0] and right[1]) and not(left[0] and left[1]):
            return [True, True, node]
        if right[0] and right[1]:
            return right
        if left[0] and left[1]:
            return left    
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.contains_p_q(root, p, q)[-1]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         stack = []
#         curr_node = root 
#         parents = {root: None}
#         while p not in parents or q not in parents:
#             if curr_node.right:
#                 parents[curr_node.right] = curr_node
#                 stack.append(curr_node.right)
#             if curr_node.left:
#                 parents[curr_node.left] = curr_node
#                 stack.append(curr_node.left)
#             curr_node = stack.pop()
#         ancestors_p = {p}
#         v = p
#         while v:
#             v = parents[v]
#             ancestors_p.add(v)
#         ans = q
#         while ans not in ancestors_p:
#             ans = parents[ans]
#         return ans
            
                
                
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     def recurse_tree(current_node):
    #         mid = (current_node == p or current_node == q)
    #         if not current_node:
    #             return False
    #         if current_node.left == None and current_node.right == None and not mid:
    #             return False
    #         left = recurse_tree(current_node.left)
    #         right = recurse_tree(current_node.right)
    #         if mid + left + right >= 2:
    #             self.ans = current_node
    #             return True
    #         return (mid or left or right)
    #     recurse_tree(root)
    #     return self.ans
        