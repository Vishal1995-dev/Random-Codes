# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ret=0
        
        def fun(node):
            nonlocal ret
            if(node==None):
                return 0
            l=fun(node.left)
            r=fun(node.right)
            val = abs(l-r)
            ret+=val
            return l+r+node.val
            
        fun(root)
        return ret
