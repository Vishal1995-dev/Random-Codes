"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        def fun(node):
            if(node==None):
                return 0
            else:
                m=0
                for i in node.children:
                    m=max(m,fun(i))
                return 1+m
        
        return fun(root)
