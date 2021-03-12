from collections import deque 

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (not root): 
            return
        q = []  
        q.append([root, 1]) 
        p={}
        while (len(q)):   
            a=q.pop(0)
            if(a[1] in p):
                p[a[1]].append(a[0])
            else:
                p[a[1]]=[a[0]]
            if (a[0].left): 
                q.append([a[0].left, a[1] + 1]) 
            if (a[0].right): 
                q.append([a[0].right, a[1] + 1 ])
        
        i=max(p)
        ret=0
        for j in p[i]:
            ret+=j.val
        return ret
