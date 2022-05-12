# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    from itertools import islice
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #split 
        if not root:
            return 'NULL'
        idx_to_node = {}
        def dfs(r, cur_idx, idx_to_node):
            new_idx = cur_idx
            new_str = ["*" + str(r.val)]
            add = ""
            if r.left:
                add = str(new_idx + 1)
                new_idx = dfs(r.left, new_idx + 1, idx_to_node)
            new_str.append(add)
            add = ""
            if r.right:
                add = str(new_idx + 1)
                new_idx = dfs(r.right, new_idx + 1, idx_to_node)
            new_str.append(add)
            idx_to_node[cur_idx] = ",".join(new_str)
            return new_idx
        end = dfs(root, 0, idx_to_node)
        ans = []
        for i in range(end + 1):
            node = idx_to_node.get(i)
            ans.append(node)
        return "".join(ans)
            

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == 'NULL':
            return []
        new_mapping = {}
        parent_to_child = {}
        # print(data)
        data = data.split('*')
        # for x in data:
        #     print(x, type(x))
        for i,x in enumerate(islice(data, 1, None)):
            val, left, right = x.split(',')
            # print(type(x))
            # print(val, left, right, i, 'dafuck')
            new_mapping[i] = TreeNode(int(val))
            parent_to_child[i] = {}
            if left != "":
                parent_to_child[i]['L'] = int(left)
            if right != "":
                parent_to_child[i]['R'] = int(right)
        for i in range(len(data) - 1):
            node = new_mapping.get(i)
            left_idx = parent_to_child.get(i).get('L')
            if left_idx:
                node.left = new_mapping.get(left_idx)
            right_idx = parent_to_child.get(i).get('R')
            if right_idx:
                node.right = new_mapping.get(right_idx)
        # print([x.val for x in new_mapping.values()])
        return new_mapping.get(0)
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))