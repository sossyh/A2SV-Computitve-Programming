# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, min_, max_):
        if root == None:
            return True
        if root.val <= min_ or root.val >= max_:
            return False
        
        lef = self.helper(root.left, min_, root.val)
        rig = self.helper(root.right, root.val, max_)
        return True if lef == True and rig == True else False
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.helper(root, float("-inf"), float("inf"))
        
        
            
            
        
        