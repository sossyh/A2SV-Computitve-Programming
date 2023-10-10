# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validate(self, root, left_bound, right_bound):
        if root.val <= left_bound or root.val >= right_bound:
            return False
        
        valid = True
        if root.left:
            valid = valid and self.validate(root.left, left_bound, root.val)
        
        if root.right:
            valid = valid and self.validate(root.right, root.val, right_bound)
        
        return valid
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, -inf, inf)
        
        
        
            
       