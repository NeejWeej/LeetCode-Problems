# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def recBinPath(self, root, ans, path):
        if not root:
            return
        path.append(str(root.val))
        if not root.right and not root.left:
            ans.append('->'.join(path))
        
        if root.right:
            self.recBinPath(root.right, ans, path)
        
        if root.left:
            self.recBinPath(root.left, ans, path)
        path.pop()
        return
            
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        ans = []
        self.recBinPath(root, ans, [])
        return ans
        
        
        
        
        
#         ans = []
#         cur_path = []
#         stack = [root]
#         cur_node = None
#         while stack:
#             cur_node = stack.pop()
#             cur_path.append(str(cur_node.val))
#             if not cur_node.left and not cur_node.right:
#                 ans.append("->".join(cur_path))
#                 cur_path.pop()
#                 continue
#             if cur_node.left:
#                 stack.append(cur_node.left)
#             if cur_node.right:
#                 stack.append(cur_node.right)
#         return ans
                
            
            