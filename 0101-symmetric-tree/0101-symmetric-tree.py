# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = []
        stack.append((root.left, root.right))
        
        while stack:
            r1, r2 = stack.pop()
            if r1 == None and r2 == None:
                continue
            if not r1 or not r2 or r2.val != r1.val:
                return False
            stack.append((r1.left, r2.right))
            stack.append((r1.right, r2.left))
            
        return True