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
    
    int maxUniValue(TreeNode* node, int val, int no) {
        if(node==NULL) return no;
        else {
            int a=no;
            int b=no;
            if(node->left!=NULL && node->left->val==val) a=maxUniValue(node->left,val,no+1);
            if(node->right!=NULL && node->right->val==val) b=maxUniValue(node->right,val,no+1);
            if(a>b) return a;
            return b;
        }
        return 0;
    }
    
    int longestUnivaluePath(TreeNode* root) {
        if(root!=NULL) {
            int r=0;
            if(root->left!=NULL && root->right!=NULL && root->left->val==root->right->val && root->left->val==root->val) {
                r=maxUniValue(root->left,root->val,0)+maxUniValue(root->right,root->val,0)+2;
            }
            else {
                r=maxUniValue(root,root->val,0);
            }
            if(r>ret) ret=r;
            longestUnivaluePath(root->left);
            longestUnivaluePath(root->right);
        }
        return ret;
    }
};
