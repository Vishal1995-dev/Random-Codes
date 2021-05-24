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
    TreeNode *first=NULL;
    TreeNode *second=NULL;
    TreeNode *prev=new TreeNode(INT_MIN);
    
    void recoverTree(TreeNode* root) {
        dfs(root);
        TreeNode* temp=new TreeNode(0);
        temp->val=first->val;
        first->val=second->val;
        second->val=temp->val;
        return;
    }
    
    void dfs(TreeNode* node) {
        if(node==NULL) return;
        dfs(node->left);
        if(first==NULL && node->val<prev->val) first=prev;
        if(first!=NULL && node->val<prev->val) second=node;
        prev=node;
        dfs(node->right);
    }
};
