# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        start, end = 0, len(values) - 1
        ans = values[start] + values[end]

        while start < end:
            ans = max(ans, values[start] + values[end])
            start += 1
            end -= 1
        
        return ans