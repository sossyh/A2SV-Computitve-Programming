# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        after = ListNode()
        before = ListNode()
        befo, aft = before, after
        while head:
            if head.val < x:
                befo.next = head
                befo = befo.next
            else:
                aft.next = head
                aft = aft.next
            head = head.next
        befo.next = after.next
        aft.next = None
        return before.next