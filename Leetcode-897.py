# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        a=[]
        def inorder(node):
            if(node!=None):
                inorder(node.left)
                a.append(node.val)
                inorder(node.right)
        inorder(root)
        head=TreeNode()
        head.val=a[0]
        temp=head
        for i in range(1,len(a)):
            temp.right=TreeNode()
            temp.right.val=a[i]
            temp=temp.right
        return head
