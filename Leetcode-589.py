"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ret=[]
        def preorder(node):
            if(root):
                ret.append(node.val)
                for i in node.children:
                    preorder(i)
        preorder(root)
        return ret
