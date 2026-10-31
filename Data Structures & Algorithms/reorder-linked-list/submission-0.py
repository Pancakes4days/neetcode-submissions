# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #find the middle
        fast, slow = head, head

        while fast.next  and fast.next.next:   
            fast = fast.next.next
            slow = slow.next

        #split
        second = slow.next
        slow.next = None

        #reverse it now
        prev, curr = None, second
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        #simply names first node "second" of second half of list
        second = prev
        
        #merge them together
        current = head
        while second:
            nxt = current.next
            current.next = second
            current = nxt
            nxt = second.next
            second.next = current
            second = nxt
        
            

        