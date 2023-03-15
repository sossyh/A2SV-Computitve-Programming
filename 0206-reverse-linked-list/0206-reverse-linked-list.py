# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(head):
            if not head or not head.next:
                return head
            rest = reverse(head.next)
            head.next.next = head
            head.next = None
            return rest
            
        return reverse(head)
            
            
