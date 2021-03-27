# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if(root==None):
            return []
        ret=[]
        a={}
        q=[]
        q.append((root,0))
        while(q):
            s=q.pop(0)
            if(s[1] not in a):
                a[s[1]]=s[0].val
            if(s[0].right!=None):
                q.append((s[0].right,s[1]+1))
            if(s[0].left!=None):
                q.append((s[0].left,s[1]+1))
        for i in a:
            ret.append(a[i])
        return ret
