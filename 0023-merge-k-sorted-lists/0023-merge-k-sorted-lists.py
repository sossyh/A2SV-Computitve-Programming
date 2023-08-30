# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        
        ans = ListNode(0)
        head = ans
        
        while heap:
            lstval, arridx, lst = heapq.heappop(heap)
            a = ListNode(lstval)
            ans.next = a
            ans = a
            
            if lst.next:
                heapq.heappush(heap, (lst.next.val, arridx, lst.next))
        
        # print(res)
        return head.next