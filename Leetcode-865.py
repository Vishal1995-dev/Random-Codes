# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        d={}
        def dfs(node,v,path):
            if(node!=None):
                s=path+[node]
                if(v in d):
                    d[v].append(s)
                else:
                    d[v]=[s]
                dfs(node.left,v+1,s)
                dfs(node.right,v+1,s)
        
        m=0
        
        dfs(root,0,[])
        for i in d:
            m=max(m,i)
            
        if(len(d[m])==1):
            return d[m][0][-1]
        
        c={}
        for i in d[m]:
            for j in i:
                if(j in c):
                    c[j]+=1
                else:
                    c[j]=1
        for i in d[m][0][::-1]:
            if(c[i]==len(d[m])):
                return i
            
