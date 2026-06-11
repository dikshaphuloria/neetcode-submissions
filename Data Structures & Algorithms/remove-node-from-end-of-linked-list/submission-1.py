# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur = head
        length = 0
        while cur:
            length+=1
            cur = cur.next

        if length - n == 0:
            return head.next

        new_link = head
        v = 0

        while new_link and new_link.next:
            if v+1 == length - n:
                new_link.next = new_link.next.next
                
            else:
                new_link = new_link.next

            v+=1
        
        return head






        