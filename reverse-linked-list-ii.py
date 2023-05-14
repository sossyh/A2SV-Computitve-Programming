# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        curr, prev = head, None
        while curr:
            net = curr.next
            curr.next = prev
            prev = curr
            curr = net
        
        return prev
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lprev, curr = dummy, head

        for _ in range(left - 1):
            lprev = lprev.next
            curr = curr.next
        
        prev = None
        for _ in range(right - left + 1):
            nxt = curr.next
            curr.next = prev
            prev = curr 
            curr = nxt

        lprev.next = prev
        
        while lprev.next:
            lprev = lprev.next
        
        lprev.next = curr

        return dummy.next