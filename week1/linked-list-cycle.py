# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Problem: checking if there is a cycle or not
                 input - head of linkedlist
        

        Solution:- floyed algorithm
                 - fast, slow = .next.next, .next
                 - if the two meet - return True
                                   - return False
        
        N =   len(linkedlist(head))
        TC: O(2N) - O(N)
        SPACE: O(1)        
        
        """

        slow, fast = head, head

        while fast and fast.next:
            
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        
        return False
