# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        
        prev = None
        curr = head
        
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        
        return prev
            
        
    def makeListNode(self, arr):
        head = ListNode(0)
        dummy = head
        
        while arr:
            a = arr.pop()
            node = ListNode(a)
            dummy.next = (node)
            dummy = dummy.next
        
        return head.next
            
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []
        newl1 = self.reverse(l1)
        newl2 = self.reverse(l2)
        carry = 0
        
        while newl1 and newl2:
            a = newl1.val + newl2.val + carry
            stack.append(a%10)
            carry = a // 10
            newl1 = newl1.next
            newl2 = newl2.next
        
        while newl1:
            a = carry + newl1.val
            stack.append(a%10)
            carry = a // 10
            newl1 = newl1.next
        
        while newl2:
            a = carry + newl2.val
            stack.append(a%10)
            carry = a // 10
            newl2 = newl2.next
        
        if carry:
            stack.append(carry)
        
        
        return self.makeListNode(stack)