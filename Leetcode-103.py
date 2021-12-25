# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        d={}
        q=[]
        ret=[]
        if(root):
            q.append((root,0))
        while(q):
            a=q.pop(0)
            if(a[1] in d):
                d[a[1]].append(a[0].val)
            else:
                d[a[1]]=[a[0].val]
            if(a[0].left):
                q.append((a[0].left,a[1]+1))
            if(a[0].right):
                q.append((a[0].right,a[1]+1))
        for i in d:
            if(i%2==0):
                ret.append(d[i])
            else:
                ret.append(d[i][::-1])
        return ret
