# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = dummy
        node = head

        while node:
            group_start = node
            kth_node = node

            for _ in range(k-1):
                if kth_node is None:
                    break
                kth_node = kth_node.next
            
            if kth_node is None:
                break
            
            group_next = kth_node.next
            kth_node.next = None

            new_head = self.reverse_one_list(group_start)

            cur.next = new_head
            group_start.next = group_next

            cur = group_start
            node = group_next
        
        return dummy.next

    
    def reverse_one_list(self, l1):
        prev = None
        cur = l1

        while cur:
            temp_node = cur.next
            cur.next = prev
            prev = cur
            cur = temp_node

        return prev







