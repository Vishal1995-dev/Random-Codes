# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        arr=[]
        arr1=[]
        
        def path(node,x):
            if(node==None):
                return False
            arr.append(node)
            if(node.val==x.val):
                return True
            if((path(node.left,x) or path(node.right,x))==True):
                return True
            arr.pop(-1)
            return False
        
        def path2(node,x):
            if(node==None):
                return False
            arr1.append(node)
            if(node.val==x.val):
                return True
            if((path2(node.left,x) or path2(node.right,x))==True):
                return True
            arr1.pop(-1)
            return False
        
        path(root,p)
        path2(root,q)
        
        m=[]
        n=[]
        if(len(arr)<len(arr1)):
            m=arr
            n=arr1
        else:
            m=arr1
            n=arr
            
        for i in range(len(m)-1,-1,-1):
            if(m[i] in n):
                return m[i]
            
