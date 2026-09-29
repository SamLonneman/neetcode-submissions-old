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
        prev = slow.next = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        # Construct final list
        list1 = head
        list2 = prev
        while list1:
            temp = list1.next
            list1.next = list2
            list1 = temp
            if list2:
                temp = list2.next
                list2.next = list1
                list2 = temp
        return head
