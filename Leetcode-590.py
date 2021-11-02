"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        ret=[]
        
        def postOrder(node):
            if(node!=None):
                for i in node.children:
                    postOrder(i)
                ret.append(node.val)
        
        postOrder(root)
        return ret
