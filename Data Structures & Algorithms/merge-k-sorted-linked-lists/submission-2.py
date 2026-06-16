# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
            
        queue = deque(node for node in lists if node)
        if not deque:
            return None

        while len(queue) > 1:
            a = queue.pop()
            b = queue.pop()
            merged = self.merge(a, b)

            queue.appendleft(merged)
        
        return queue.pop()

    def merge(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            v1 = l1.val
            v2 = l2.val
            if v1 > v2:
                cur.next = ListNode(v2)
                l2 = l2.next
            else:
                cur.next = ListNode(v1)
                l1 = l1.next
            cur = cur.next

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return dummy.next
                

        
        