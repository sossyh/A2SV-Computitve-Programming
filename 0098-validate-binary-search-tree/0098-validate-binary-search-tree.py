# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        
        stack = [(root, float("-inf"), float("inf"))]
        
        while stack:
            ans, min_, max_ = stack.pop()
            if ans == None:
                continue
            if ans.val <= min_ or ans.val >= max_:
                return False
            
            stack.append((ans.left, min_, ans.val))
            stack.append((ans.right, ans.val, max_))  
            
        return True