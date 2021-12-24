# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    ans=0
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans=0
        def fun(node):
            if(node==None):
                return 0
            left=fun(node.left)
            right=fun(node.right)
            self.ans=max(self.ans,left+right)
            return 1+max(left,right)
            
        fun(root)
        return self.ans
