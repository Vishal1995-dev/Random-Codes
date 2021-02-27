"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        a=[]
        temp=head
        n=Node()
        while(temp!=None):
            if(temp.child==None):
                n=temp
                temp=temp.next
            else:
                a.append(temp.next)
                temp.next=temp.child
                temp.next.prev=temp
                temp.child=None
                n=temp
                temp=temp.next
        a.reverse()
        for i in a:
            if(i == None):
                continue
            n.next=i
            i.prev=n
            while(n.next!=None):
                n=n.next
        return head
