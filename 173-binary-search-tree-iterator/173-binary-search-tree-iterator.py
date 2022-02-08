# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.new_sorted_arr(root, self.arr)
        # self.arr = self.get_sorted(root)
        self.len = len(self.arr)
        self.idx = 0

    def next(self) -> int:
        ans = self.arr[self.idx]
        self.idx += 1
        return ans

    def hasNext(self) -> bool:
        if self.len == self.idx:
            return False
        return True
    
    def new_sorted_arr(self, root, arr):
        if not root:
            return
        self.new_sorted_arr(root.left, arr)
        arr.append(root.val)
        self.new_sorted_arr(root.right, arr)
        return
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()