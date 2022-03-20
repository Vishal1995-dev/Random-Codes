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
        flag=0
        while(q):
            l=len(q)
            v=q.pop(0)
            if(v.left):
                q.append(v.left)
            if(v.right):
                q.append(v.right)
            i=1
            if(flag==0):
                if(v.val%2==0):
                    return False
                while(i<l):
                    val=q.pop(0)
                    if(val.val%2==0 or val.val<=v.val):
                        return False
                    if(val.left):
                        q.append(val.left)
                    if(val.right):
                        q.append(val.right)
                    v=val
                    i+=1
                flag=1
            else:
                if(v.val%2==1):
                    return False
                while(i<l):
                    val=q.pop(0)
                    if(val.val%2==1 or val.val>=v.val):
                        return False
                    if(val.left):
                        q.append(val.left)
                    if(val.right):
                        q.append(val.right)
                    v=val
                    i+=1
                flag=0
        return True
                
