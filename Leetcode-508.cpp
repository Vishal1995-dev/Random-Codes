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
    map<int,int>c;
    int m=0;
    
    int sum(TreeNode* node) {
        if(node==NULL) return 0;
        int v=sum(node->left)+sum(node->right)+node->val;
        c[v]++;
        if(c[v]>m) m=c[v];
        return v;
    }
    
    vector<int> findFrequentTreeSum(TreeNode* root) {
        sum(root);
        vector<int>ret;
        for(auto i:c) {
            if(i.second==m) ret.push_back(i.first);
        }
        return ret;
    }
};
