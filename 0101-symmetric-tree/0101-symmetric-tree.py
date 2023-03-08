# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def areSame(self, p, q):
        
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        leftpart = self.areSame(p.left, q.right)
        rightpart = self.areSame(p.right, q.left)
        
        return True if leftpart == True and rightpart == True else False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.areSame(root.left, root.right)