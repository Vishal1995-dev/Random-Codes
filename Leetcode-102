# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(root==None):
            return []
        
        lev={}
        
        def level(l,node):
            if(node==None):
                return
            if(l in lev):
                lev[l].append(node.val)
            else:
                lev[l]=[node.val]
                
            level(l+1,node.left)
            level(l+1,node.right)
        
        lev[1]=[root.val]
        level(2,root.left)
        level(2,root.right)
        
        ret=[]
        lev = OrderedDict(sorted(lev.items()))
        for i in range(len(lev)):
            ret.append(lev[i+1])
        return ret
