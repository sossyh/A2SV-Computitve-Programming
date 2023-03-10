# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root , min_, max_):
        if not root:
            return True
        if root.val <= min_ or root.val >= max_:
            return False
        
        
        left = self.helper(root.left, min_, root.val)
        right = self.helper(root.right, root.val, max_)
        
        return (left and right)
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, float("-inf"), float("inf"))
        
        
            
       