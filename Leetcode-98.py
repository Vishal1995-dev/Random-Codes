# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):   
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        
        def helper(node,l=float('-inf'),h=float('inf')):
            if not node:
                return True
            
            val=node.val
            print(val,l,h)
            if(val<=l or val>=h):
                return False
            
            if not helper(node.right,val,h):
                return False
            if not helper(node.left,l,val):
                return False
            return True
        
        return helper(root)
        """
        
        stack,inorder=[],float('-inf')
        
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            if root.val<=inorder:
                return False
            inorder=root.val
            root=root.right
            
        return True
        
