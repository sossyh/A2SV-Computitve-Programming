# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.sums = 0
        
        def helper(root):
            if not root.left and not root.right:
                return root.val
            
            lefttree = helper(root.left) if root.left else 0
            righttree = helper(root.right) if root.right else 0
            self.sums += abs(lefttree - righttree)
            
            return lefttree + righttree + root.val
        
        helper(root)
        return self.sums