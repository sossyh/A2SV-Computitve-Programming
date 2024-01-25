# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = 0
        queue = deque()
        queue.append(root)
        
        while queue:
            item = queue.popleft()
            if item.val >= low and item.val <= high:
                ans += item.val
            
            if item.left:
                queue.append(item.left)
            
            if item.right:
                queue.append(item.right)
        
        return ans