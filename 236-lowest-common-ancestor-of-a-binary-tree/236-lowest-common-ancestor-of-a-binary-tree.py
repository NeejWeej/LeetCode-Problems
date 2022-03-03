# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None
        
    # def contains_p_q(self, node, p, q):
    #     ans = [False, False]
    #     if node.val == p.val:
    #         ans[0] = True
    #     elif node.val == q.val:
    #         ans[1] = True
    #     right = [False, False]
    #     left = [False, False]
    #     if node.right:
    #         right = self.contains_p_q(node.right, p, q)
    #         if right[0] and right[1]:
    #             return right
    #     if node.left:
    #         left = self.contains_p_q(node.left, p, q)
    #         if left[0] and left[1]:
    #             return left
    #     ans[0] = ans[0] or right[0] or left[0]
    #     ans[1] = ans[1] or right[1] or left[1]
    #     if not(ans[0] and ans[1]):
    #         return [ans[0], ans[1], None]
    #     if not(right[0] and right[1]) and not(left[0] and left[1]):
    #         return [True, True, node]
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur_path = [[root, 0]]
        stack = []
        
        p_path = []
        q_path = {}
        
        while True:
            node, children_visited = cur_path[-1][:]
            if node.val == q.val:
                q_path = {x.val:x for x,c_v in cur_path}
                if len(q_path) > 0 and len(p_path) > 0:
                    break
            if node.val == p.val:
                p_path = [x for x, c_v in cur_path]
                if len(q_path) > 0 and len(p_path) > 0:
                    break
                
            if children_visited == 0:
                if node.left:
                    cur_path[-1][-1] = 1
                    cur_path.append([node.left, 0])
                    continue
                elif node.right:
                    cur_path[-1][-1] = 2
                    cur_path.append([node.right, 0])
                    continue
                else:
                    cur_path.pop()
            elif children_visited == 1:
                if node.right:
                    cur_path[-1][-1] = 2
                    cur_path.append([node.right, 0])
                    continue
                else:
                    cur_path.pop()
            else:
                cur_path.pop()
        
        for node in reversed(p_path):
            if node.val in q_path:
                return node
            
                
                
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
        