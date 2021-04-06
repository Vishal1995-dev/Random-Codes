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
    void preorder(TreeNode* node,TreeNode* head)
    {
        if(node!=NULL)
        {
            head->val=node->val;
            if(node->left!=NULL) 
            {
                TreeNode* node2 = new TreeNode();
                head->right=node2;
                preorder(node->left,head->right);
            }
            if(node->right!=NULL) 
            {
                TreeNode* node2 = new TreeNode();
                while(head->right!=NULL)
                {
                    head=head->right;
                }
                head->right=node2;
                preorder(node->right,head->right);
            }
        }
    }
    
    void flatten(TreeNode* root) {
        if(root==NULL) return;
        TreeNode* head = new TreeNode();
        preorder(root,head);
        *root=*head;
        return;
    }
};
