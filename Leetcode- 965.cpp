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
    bool check(TreeNode* node,int value)
    {
        if(node==NULL) return true;
        if(node->val!=value) return false;
        return check(node->left,value) && check(node->right,value);
    }
    
    bool isUnivalTree(TreeNode* root) {
        int value=root->val;
        return check(root,value);
    }
};
