# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ans = 0
        
        def dfs(root, summ):
            nonlocal ans
            if not root.right and not root.left:
                summ += str(root.val)
                ans += int(summ, 2)
                return
            
            summ += str(root.val)
            
            if root.left:
                dfs(root.left, summ)
            
            if root.right:
                dfs(root.right, summ)
            
        
        dfs(root, "")
        
        return ans