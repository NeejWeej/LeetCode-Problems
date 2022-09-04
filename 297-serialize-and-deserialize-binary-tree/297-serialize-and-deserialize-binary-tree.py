# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def recSearch(self, node, ans):
        if not node:
            ans.append('$')
            ans.append(",")
            return
        ans.append(str(node.val))
        ans.append(",")
        self.recSearch(node.left, ans)
        self.recSearch(node.right, ans)
    
    def recDeserialize(self, dataI):
        vals = [next(dataI)]
        while vals[-1] != ",":
            vals.append(next(dataI))
        vals.pop()
        if len(vals) == 1 and vals[0] == '$':
            return None
        newVal = int("".join(vals))
        node = TreeNode(newVal)
        node.left = self.recDeserialize(dataI)
        node.right = self.recDeserialize(dataI)
        return node
        

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ans = []
        self.recSearch(root, ans)
        return "".join(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        dataI = iter(data)
        # return None
        return self.recDeserialize(dataI)
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))