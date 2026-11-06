# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
    # cut in half

        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        curr = head

        cutoff = length // 2

        for i in range(cutoff):
            curr = curr.next

        new = curr.next
        curr.next = None

        # reverse second half
        prev, header = None, new

        while header:
            nxt = header.next
            header.next = prev
            prev = header
            header = nxt

        new = prev
        
        # combine time

        dummy = tail = ListNode()

        while new and head:

            tail.next = head
            tail = tail.next
            head = head.next

            tail.next = new
            tail = tail.next
            new = new.next
        tail.next = new or head