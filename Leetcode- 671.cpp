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
    set<int> a;
    
    void dfs(TreeNode* node) {
        if(node!=NULL) {
            a.insert(node->val);  
            dfs(node->left);
            dfs(node->right);
        }
        return;
    }
    int findSecondMinimumValue(TreeNode* root) {
        
        dfs(root);
        vector<int>v(a.begin(),a.end());
        sort(v.begin(),v.end());
        
        if(v.size()<2) return -1;
        return v[1];
    }
};
