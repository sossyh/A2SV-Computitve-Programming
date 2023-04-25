# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        oddpt, evenpt = odd, even
        count = 0

        while head:
            if count % 2 == 0:
                evenpt.next = head
                evenpt = evenpt.next
            else:
                oddpt.next = head
                oddpt = oddpt.next
            head = head.next
            count += 1

        evenpt.next = odd.next
        oddpt.next = None
        return even.next