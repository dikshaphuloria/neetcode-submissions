# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        values = list(node for node in lists if node)
        if not values:
            return None

        while len(values) > 1:
            a = values.pop()
            b = values.pop()
            merged = self.merge(a, b)

            values.append(merged)
        
        return values.pop()

    def merge(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            else:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            cur = cur.next

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return dummy.next
                

        
        