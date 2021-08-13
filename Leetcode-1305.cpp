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
    vector<int>ret;
        
    void getNodes(TreeNode* node) {
        ret.push_back(node->val);
        if(node->left!=NULL) getNodes(node->left);
        if(node->right!=NULL) getNodes(node->right);
    } 
    
    vector<int> getAllElements(TreeNode* root1, TreeNode* root2) {
        if(root1!=NULL)
            getNodes(root1);
        if(root2!=NULL)
            getNodes(root2);
        sort(ret.begin(),ret.end());
        return ret;
    }
};
