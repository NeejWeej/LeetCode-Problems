# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque([(root, 0)])
        last_depth = -1
        ans = []
        
        while len(q) > 0:
            new_node, depth = q.popleft()
            if depth > last_depth:
                ans.append([])
                last_depth = depth
            ans[-1].append(new_node.val)
            left_child = new_node.left
            right_child = new_node.right
            if left_child:
                q.append( (left_child, depth + 1) )
            if right_child:
                q.append( (right_child, depth + 1) )
            # if depth % 2 == 1:
            #     if left_child:
            #         q.append( (left_child, depth + 1) )
            #     if right_child:
            #         q.append( (right_child, depth + 1) )
            # else:
            #     if right_child:
            #         q.append( (right_child, depth + 1) )
            #     if left_child:
            #         q.append( (left_child, depth + 1) )
        for i in range(1, len(ans), 2):
            ans[i] = ans[i][::-1]
        return ans