# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1 = len1 = 0
        nums2 = len2 = 0
        
        while l1:
            len1+=1
            nums1+= l1.val * (10**len1)
            l1 = l1.next

        while l2:
            len2+=1
            nums2+= l2.val * (10**len2)
            l2 = l2.next

        dummy = ListNode(0)
        cur = dummy
        result = nums1 + nums2

        if result%10 == 0:
            result = result//10

        result = str(result)
        result2 = result[::-1]


        for s in result2:
            cur.next = ListNode(int(s))
            cur = cur.next

        return dummy.next


        





        


        