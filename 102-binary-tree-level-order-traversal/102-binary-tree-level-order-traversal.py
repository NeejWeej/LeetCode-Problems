# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import deque
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while len(q) > 0:
            new_layer = deque([])
            this_level = []
            for _ in range(len(q)):
                cur = q.popleft()
                this_level.append(cur.val)
                if cur.left:
                    new_layer.append(cur.left)
                if cur.right:
                    new_layer.append(cur.right)
            ans.append(this_level)
            q = new_layer
        return ans
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

        
        # if root is None:
        #     return []
        # result = [[]]
        # curr_level = collections.deque([root])
        # # curr_level = [root]
        # next_level = collections.deque([])  
        # while len(curr_level) > 0 or len(next_level) > 0:
        #     if len(curr_level) == 0:
        #         curr_level, next_level = next_level, curr_level
        #         result.append([])
        #     curr_node = curr_level.popleft()
        #     if curr_node.left is not None:
        #         next_level.append(curr_node.left)
        #     if curr_node.right is not None:
        #         next_level.append(curr_node.right)
        #     result[-1].append(curr_node.val)
        # return result
        