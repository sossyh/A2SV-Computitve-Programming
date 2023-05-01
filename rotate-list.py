# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        inans = head
        fast = head
        slow = head
        i = 0
        while head and head.next:
            i += 1
            head = head.next
        i += 1
        if k % i == 0 or i == 1:
            return inans

        k = k % i
        m = i - k
        j = 1
        while fast and j <= m:
            j += 1
            fast = fast.next
        
        ans = fast
        while fast and fast.next:
            fast = fast.next
        fast.next = slow

        n = 1
        while slow and n < m:
            n += 1
            slow = slow.next

        slow.next = None
       
        return ans