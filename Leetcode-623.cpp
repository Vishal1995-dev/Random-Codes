/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(inthttps://assets.leetcode.com/uploads/2021/03/15/addrow-tree.jpg x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
       queue<pair<TreeNode*,int>> q;
        if(depth==1)
        {
            TreeNode* node=new TreeNode(val);
            node->left=root;
            return node;
        }
        q.push(pair{root,1});
        while(!q.empty())
        {
            pair<TreeNode*,int>p=q.front();
            q.pop();
            if(p.second==depth-1)
            {
                TreeNode* node=new TreeNode(val);
                node->left=p.first->left;
                p.first->left=node;

                TreeNode* node1=new TreeNode(val);
                node1->right=p.first->right;
                p.first->right=node1;
            }
            else
            {
                if(p.first->left!=NULL)
                    q.push(pair{p.first->left,p.second+1});
                if(p.first->right!=NULL)
                    q.push(pair{p.first->right,p.second+1});
            }
        }
        return root;
    }
};
