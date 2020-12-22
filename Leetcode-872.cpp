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
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> l1;
        vector<int> l2;
        
        dfs(root1,l1);
        dfs(root2,l2);
        
        return l1==l2;
    }
    
    void dfs(TreeNode* node,vector<int>& l)
    {
        if(node==NULL) return;
        if(node->left==NULL && node->right==NULL)
            l.push_back(node->val);
        dfs(node->left,l);
        dfs(node->right,l);
    }
};
