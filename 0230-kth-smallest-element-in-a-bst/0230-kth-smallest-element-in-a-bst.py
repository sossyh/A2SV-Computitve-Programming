# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []
        queue =  deque()
        queue.append(root)
        
        while queue:
            item = queue.popleft()
            result.append(item.val)
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        
        result.sort()
        return result[k-1]
        