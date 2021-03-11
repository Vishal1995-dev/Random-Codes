# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        a=[]
        
        def inorder(node):
            if(node!=None):
                inorder(node.left)
                a.append(node.val)
                inorder(node.right)
                
        inorder(root)
        for i in a:
            if((k-i) in a and (k-i)!=i):
                return True
        return False
