# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution(object):
    a=[]
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.a=[]
        while(head!=None):
            self.a.append(head.val)
            head=head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        return random.choice(self.a) 


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
