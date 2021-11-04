"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        level={}
        
        def bfs(node):
            q=[]
            q.append([node,0])
            while(q):
                v=q.pop(0)
                if(v[0]!=None):
                    if(v[1] in level):
                        level[v[1]].append(v[0])
                    else:
                        level[v[1]]=[v[0]]
                    q.append([v[0].left,v[1]+1])
                    q.append([v[0].right,v[1]+1])
        
        bfs(root)
        for i in level:
            node=level[i][0]
            for j in range(1,len(level[i])):
                node.next=level[i][j]
                node=node.next
        return root
        
