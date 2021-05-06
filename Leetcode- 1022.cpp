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
    int ret=0;
    void traverse(TreeNode* node,int curr)
    {
        if(node!=NULL)
        {
            curr=(curr<<1)|node->val;
            if(node->left==NULL && node->right==NULL) ret+=curr;
            traverse(node->left,curr);
            traverse(node->right,curr);
        }
    }
    
    int sumRootToLeaf(TreeNode* root) {
        traverse(root,0);
        return ret;
    }
};
