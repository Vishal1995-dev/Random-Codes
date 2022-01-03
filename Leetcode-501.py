# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    m=0
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d={}
        self.m=0
        def dfs(node):
            if(node):
                if(node.val in d):
                    d[node.val]+=1
                else:
                    d[node.val]=1
                self.m=max(self.m,d[node.val])     
                dfs(node.right)
                dfs(node.left)
        
        dfs(root)
        ret=[]
        for i in d:
            if(d[i]==self.m):
                ret.append(i)
        return ret
