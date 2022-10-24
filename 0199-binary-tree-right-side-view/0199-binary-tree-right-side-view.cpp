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
    vector<int> rightSideView(TreeNode* root) {
        vector<TreeNode*> st;
        vector<int>ans;
        if (!root) return ans;
        
        st.push_back(root);
        while(!st.empty()){
            ans.push_back(st.back()->val);
            vector<TreeNode*>newSt;
            for(auto& b: st){
                if(b->left) newSt.push_back(b->left);
                if(b->right) newSt.push_back(b->right);
            }
            st = newSt;
        }
        return ans;
        
    }
};