# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        
        def rights(root):
            queue = deque()
            queue.append(root)
            
            while queue:
                n = len(queue) 
                k = []
                for i in range(n):
                    item = queue.popleft()
                    if item.left:
                        queue.append(item.left)
                    if item.right:
                        queue.append(item.right)
                    if i == n-1:
                        result.append(item.val)
                
        rights(root)
        
        return result