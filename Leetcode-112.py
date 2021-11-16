# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def check(node,s):
            if(node!=None):
                s+=node.val
                if(node.left==None and node.right==None):
                    if(s==targetSum):
                        return True
                    else:
                        return False
                a=b=False
                if(node.left!=None):
                    a=check(node.left,s)
                if(node.right!=None):
                    b=check(node.right,s)
                return a or b
        
        if(root==None):
            return False
        if(root.left==None and root.right==None):
            return root.val==targetSum
        return check(root.left,root.val) or check(root.right,root.val)
        
        
