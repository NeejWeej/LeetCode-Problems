# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class HeightNode:
    def __init__(self, node, isLeft):
        self.node = node
        self.isLeft = isLeft
        self.status = 2
        self.leftH = 0
        self.rightH = 0
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        stack = [HeightNode(root, True)]
        while stack:
            last = stack[-1]
            if last.status == 2:
                last.status -= 1
                if last.node.left:
                    stack.append(HeightNode(last.node.left, True))
                    
            elif last.status == 1:
                last.status -= 1
                if last.node.right:
                    stack.append(HeightNode(last.node.right, False))
                    
            else:
                if abs(last.leftH - last.rightH) > 1:
                    return False
                height = 1 + max(last.leftH, last.rightH)
                stack.pop()
                if not stack:
                    return True
                if last.isLeft:
                    stack[-1].leftH = height  
                else:
                    stack[-1].rightH = height
        return True
                
            
            
        