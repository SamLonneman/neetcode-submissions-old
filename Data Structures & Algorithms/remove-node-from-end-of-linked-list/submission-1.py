# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        current = dummy
        c = 0
        while current.next:
            current = current.next
            c += 1
        
        current = dummy
        i = c
        while i > n:
            current = current.next
            i -= 1
        current.next = current.next.next
        return dummy.next