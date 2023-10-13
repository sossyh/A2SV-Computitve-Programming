# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        
        def dfs(root):
            if not root:
                return 0
            
            left_child = dfs(root.left)
            right_child = dfs(root.right)
            
            self.count += abs(left_child) + abs(right_child)
            
            result = root.val + left_child + right_child - 1
            
            return result
        
        dfs(root)
        
        return self.count
        