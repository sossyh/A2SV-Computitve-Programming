# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def traversal(node):
            if not node.left and not node.right:
                return False if node.val == 0 else 1
            
            left = traversal(node.left)
            right = traversal(node.right)
            
            return (left and right) if node.val == 3 else (left or right)
        
        return traversal(root)