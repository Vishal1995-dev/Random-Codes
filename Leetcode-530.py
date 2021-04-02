# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        a=[]
        def traverse(node):
            if(node==None):
                return
            a.append(node.val)
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        a.sort()
        ret=a[-1]
        for i in range(1,len(a)):
            ret=min(ret,a[i]-a[i-1])
        return ret
