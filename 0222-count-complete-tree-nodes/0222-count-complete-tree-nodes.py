# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        totalnodes = 0
        queue = deque()
        queue.append(root)
        
        while queue:
            item = queue.popleft()
            totalnodes += 1
            
            if item.left:
                queue.append(item.left)
            
            if item.right:
                queue.append(item.right)
        
        return totalnodes