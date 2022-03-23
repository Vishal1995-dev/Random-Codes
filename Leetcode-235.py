# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        p=p.val
        q=q.val
        
        def dfs(node):
            if(node.val==p or node.val==q):
                return node
            elif((node.val>p and node.val<q) or (node.val<p and node.val>q)):
                return node
            elif(node.val>p and node.val>q):
                return dfs(node.left)
            else:
                return dfs(node.right)
        
        return dfs(root)
