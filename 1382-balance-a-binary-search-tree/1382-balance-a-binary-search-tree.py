# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inOrder(self, node, arr):
        if node.left:
            self.inOrder(node.left, arr)
        arr.append(node)
        if node.right:
            self.inOrder(node.right, arr)
    
    def newTree(self, arr):
        n = len(arr)
        if n == 0:
            return None
        mid = n//2
        node = arr[mid]
        node.left = self.newTree(arr[:mid])
        node.right = self.newTree(arr[mid + 1:])
        return node
        
    def balanceBST(self, root: TreeNode) -> TreeNode:
        sorted_arr = []
        self.inOrder(root, sorted_arr)
        return self.newTree(sorted_arr)
        
        