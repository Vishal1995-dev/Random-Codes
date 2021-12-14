# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ret=None
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        def check(node1,node2):
            if(node1!=None):
                if(node1 is target):
                    self.ret=node2
                check(node1.left,node2.left)
                check(node1.right,node2.right)
            return
        
        check(original,cloned)
        return self.ret
