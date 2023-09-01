# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        first, second = inf, inf
        
        queue = deque()
        queue.append(root)
        
        while queue:
            item = queue.popleft()
            if item.val < first:
                second = first
                first = item.val
            elif item.val > first and item.val < second:
                second = item.val
            
            if item.left:
                queue.append(item.left)
            
            if item.right:
                queue.append(item.right)
        
        return second if second != inf else -1