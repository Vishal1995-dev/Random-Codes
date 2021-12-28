# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret=[]
        
        def path(node,p):
            if(node!=None):
                if(node.left==None and node.right==None):
                    p.append(str(node.val))
                    s="->".join(p)
                    ret.append(s)
                else:
                    path(node.left,p+[str(node.val)])
                    path(node.right,p+[str(node.val)])
        
        path(root,[])
        return ret
