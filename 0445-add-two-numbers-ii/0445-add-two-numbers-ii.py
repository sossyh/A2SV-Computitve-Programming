# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev, curr = None, head
        
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        
        return prev
    
    def make_linkedlist(self, stack):
        head = ListNode()
        dummy =  head
        
        while stack:
            val = stack.pop()
            dummy.next = ListNode()
            dummy.next.val = val
            dummy = dummy.next
        
        return head.next
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        stack = []
        
        carry = 0
        
        
        while l1 and l2:
            total = l1.val + l2.val + carry
            stack.append(total % 10)
            carry = total // 10
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total = l1.val + carry
            stack.append(total % 10)
            carry = total // 10
            l1 = l1.next
        
        while l2:
            total = l2.val + carry
            stack.append(total % 10)
            carry = total // 10
            l2 = l2.next
        
        if carry:
            stack.append(carry)
        
        return (self.make_linkedlist(stack))
       