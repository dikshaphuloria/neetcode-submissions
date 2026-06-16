# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = [l for l in lists if l]

        if not nodes:
            return None

        while len(nodes) > 1:
            a = nodes.pop()
            b = nodes.pop()
            merged = self.merge(a, b)

            nodes.insert(0, merged)
        
        return nodes[0]

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
                

        
        