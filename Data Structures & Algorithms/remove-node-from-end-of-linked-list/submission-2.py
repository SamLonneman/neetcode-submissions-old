# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Create a dummy node whose next is head
        dummy = ListNode(0, head)

        # Create a left and right pointer
        left = dummy
        right = dummy

        # Move the right pointer forward by n
        while n > 0:
            right = right.next
            n -= 1
        
        # Move both pointers until right reaches the end
        while right.next:
            right = right.next
            left = left.next
        
        # Left pointer is now n from the end, remove the next one
        left.next = left.next.next

        # Return dummy.next
        return dummy.next
