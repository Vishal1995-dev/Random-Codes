# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isEvenOddTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q=[]
        q.append(root)
        flag=True
        while(q):
            prev=None
            for _ in range(len(q)):
                v=q.pop(0)
                if(flag):
                    if(v.val%2==0):
                        return False
                    if(prev and prev.val>=v.val):
                        return False
                else:
                    if(v.val%2==1):
                        return False
                    if(prev and prev.val<=v.val):
                        return False
                if(v.left):
                    q.append(v.left)
                if(v.right):
                    q.append(v.right)
                prev=v
            flag=not flag
        return True
