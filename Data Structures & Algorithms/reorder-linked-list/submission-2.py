# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find middle
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse everything after middle
        node = slow.next
        slow.next = None
        prev = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        # Construct final list
        list1 = head
        list2 = prev
        while list2:
            temp1, temp2 = list1.next, list2.next
            list1.next = list2
            list2.next = temp1
            list1, list2 = temp1, temp2
        return head
