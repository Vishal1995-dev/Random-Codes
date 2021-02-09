# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        
        if(head==None or head.next==None or head.next.next==None):
            return
        temp=head
        while(temp!=None):
            temp2=temp.next
            flag=0
            while(temp2!=None and temp2.next!=None and temp2.next.next!=None):
                temp2=temp2.next
                flag=1
            if(temp2!=None and temp2.next!=None and flag==0):
                temp2.next.next=temp.next
                temp.next=temp2.next
                temp2.next=None
                temp=temp.next.next
            if(flag==1):    
                temp2.next.next=temp.next
                temp.next=temp2.next
                temp2.next=None
                temp=temp.next.next
            else:
                return
        return
        """
        a=[]
        temp=head
        while(temp!=None):
            a.append(temp)
            temp=temp.next
        if(len(a)<3):
            return
        i=0
        j=len(a)-1
        while(j>i):
            a[i].next=a[j]
            a[j].next=a[i+1]
            i+=1
            j-=1
        a[i].next=None
        return
