# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        Dic = {}
        pos = 0
        while head:
            if head in Dic:
                return True
            Dic[head] = pos
            head = head.next
            pos += 1
        return False