# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        stack = [(root,[root.val], root.val)]
        while stack:
            cur_node, path, cur_sum = stack.pop()
            if cur_sum == targetSum and not cur_node.left and not cur_node.right:
                ans.append(path)
            if cur_node.left:
                new_path = [x for x in path]
                new_path.append(cur_node.left.val)
                new_sum = cur_sum + cur_node.left.val
                to_add = (cur_node.left, new_path, new_sum)
                stack.append(to_add)
            if cur_node.right:
                new_path = [x for x in path]
                new_path.append(cur_node.right.val)
                new_sum = cur_sum + cur_node.right.val
                to_add = (cur_node.right, new_path, new_sum) 
                stack.append(to_add)
        return ans
        