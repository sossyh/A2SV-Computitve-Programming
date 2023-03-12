# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        width = 0
        queue = deque()
        queue.append((root, 1))
        
        while queue:
            mini, maxi = float("inf"), float("-inf")
            for i in range(len(queue)):
                a, idx = queue.popleft()
                mini = min(mini, idx)
                maxi = max(maxi, idx)
                if a.left:
                    idxl = 2 * idx
                    queue.append((a.left, idxl))
                if a.right:
                    idxr = (2 * idx) + 1
                    queue.append((a.right, idxr))
        
            width = max(width, maxi - mini + 1)
            
        return width
            
                
            
            
            