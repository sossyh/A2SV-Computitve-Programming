# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        result = []
        curr = head
        while curr:
            result.append(0)
            curr = curr.next
        
        idxstack = []
        stack = []
        count = 0
        while head:
            while stack and stack[-1] < head.val:
                value = stack.pop()
                idx = idxstack.pop()
                result[idx] = head.val
            stack.append(head.val)
            idxstack.append(count)
            count += 1
            head = head.next
        
        return result