# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, r1, r2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if(not r1):
            return r2
        if(not r2):
            return r1
        r1.val+=r2.val
        r1.left=self.mergeTrees(r1.left,r2.left)
        r1.right=self.mergeTrees(r1.right,r2.right)
        return r1
