# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, root):
        prev, curr = None, root
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        
        return prev
        
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        head = self.reverse(head)
        dummy = head
        carry =  0
        prev = None
        
        while head:
            value = 2 * head.val  + carry
            head.val = value % 10
            carry = value // 10
            prev = head
            head = head.next
        
        if carry:
            prev.next = ListNode(carry)
        
        return self.reverse(dummy)
        
        