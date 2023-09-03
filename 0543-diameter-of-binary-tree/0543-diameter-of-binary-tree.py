# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = -inf
        
        def dfs(root):
            nonlocal ans
            if not root.left and not root.right:
                return 1
            
            a = 0
            if root.left:
                a = dfs(root.left)
            
            b = 0
            if root.right:
                b = dfs(root.right)
            
            ans = max(ans, a+b)
            
            return max(a,b)+1
        
        dfs(root)
        
        return ans if ans != -inf else 0
        
                
                
            
            