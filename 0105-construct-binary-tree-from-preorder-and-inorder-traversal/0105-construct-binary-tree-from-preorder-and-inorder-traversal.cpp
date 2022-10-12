/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        map<int, int> inorderPos;
        int n = inorder.size();
        for(int i = 0; i < n; ++i) inorderPos[inorder[i]] = i;
        int start = 0;
        return helper(preorder, inorder, start, 0, n - 1, inorderPos);
        
    }
    
    TreeNode* helper(vector<int>& preorder, vector<int>& inorder, int& idx, int iS, int iE, map<int, int>& mp){
        if (iS > iE || idx >= preorder.size()) return NULL;
        int rootval = preorder[idx];
        TreeNode* root = new TreeNode(rootval, static_cast<TreeNode*>(NULL), static_cast<TreeNode*>(NULL));
        ++idx;
        int inSpot = mp[rootval];
        root->left = helper(preorder, inorder, idx, iS, inSpot - 1, mp);
        root->right = helper(preorder, inorder, idx, inSpot + 1, iE, mp);
        return root;
    }
    
};