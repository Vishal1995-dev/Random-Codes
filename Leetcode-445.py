# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1=''
        s2=''
        temp=l1
        while(temp!=None):
            s1+=str(temp.val)
            temp=temp.next
        temp=l2
        while(temp!=None):
            s2+=str(temp.val)
            temp=temp.next
        r=str(int(s1)+int(s2))
        l=ListNode(r[0])
        temp=l
        for i in range(1,len(r)):
            temp1=ListNode(r[i])
            temp.next=temp1
            temp=temp.next
        return l
