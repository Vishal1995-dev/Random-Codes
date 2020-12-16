# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head==None):
            return None
        a=[]
        a.append(head)
        temp=head.next
        while(temp!=None):
            if(temp in a):
                return temp
            else:
                a.append(temp)
            temp=temp.next
        return None
