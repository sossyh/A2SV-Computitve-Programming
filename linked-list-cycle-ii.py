# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = {}
        prev = head
        while head:
            if head in d:
                return head
            d[head] = 1
            prev = head
            head = head.next
        return None