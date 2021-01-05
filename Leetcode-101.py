# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self,n1,n2):
        if(n1==None and n2==None):
            return True
        if(n1==None or n2==None):
            return False
        return n1.val==n2.val and self.check(n1.right,n2.left) and self.check(n2.right,n1.left)
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root,root)
