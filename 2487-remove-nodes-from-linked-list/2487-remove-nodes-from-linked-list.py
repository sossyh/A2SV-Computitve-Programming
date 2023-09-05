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
    
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        stack = []
        
        while head:
            while stack and stack[-1] < head.val:
                stack.pop()
            
            stack.append(head.val)
            head = head.next
       
        dummy = ListNode(0)
        ans = dummy
        
        while stack:
            a = stack.pop()
            dummy.next = ListNode(a)
            dummy = dummy.next
        
        
        return self.reverse(ans.next)
        