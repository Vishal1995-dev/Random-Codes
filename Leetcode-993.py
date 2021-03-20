# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if(x==root.val or y==root.val):
            return False
        s1=0
        s2=0
        parent1=0
        parent2=0
        q=deque()
        q.append((root,0))
        while(q):
            node=q.popleft()
            if(node[0]==None):
                continue
            if(node[0].val==x):
                s1=node[1]
                parent1=node[2]
            if(node[0].val==y):
                s2=node[1]
                parent2=node[2]
            if(s1!=0 and s2!=0):
                return (s1==s2 and parent1!=parent2)
            q.append((node[0].left,node[1]+1,node[0].val))
            q.append((node[0].right,node[1]+1,node[0].val))
        return (s1==s2)
