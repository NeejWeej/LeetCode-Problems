# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections  
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        col_to_node = {}
        if not root:
            return []
        q = [[root, 0]]
        min_col = 0
        max_col = 0
        while len(q) > 0:
            layer = []
            for node, col in q:
                col_list = col_to_node.get(col, [])
                col_list.append(node.val)
                col_to_node[col] = col_list
                min_col = min(col, min_col)
                max_col = max(col, max_col)
                if node.left:
                    layer.append((node.left, col - 1))
                if node.right:
                    layer.append((node.right, col + 1))
            q = layer
        sorted_cols = [[] for _ in range(1 + max_col - min_col)]
        for idx, list_of_nodes in col_to_node.items():
            sorted_cols[idx - min_col] = list_of_nodes

        ans = [x for x in sorted_cols if len(x) > 0]
        return ans
        
                