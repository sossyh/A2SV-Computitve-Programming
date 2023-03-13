# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        
        def ave(root):
            if not root:
                return (0, 0)
            else:
                left = ave(root.left)
                right = ave(root.right)
                sums = left[0] + right[0] + root.val
                number = left[1] + right[1] + 1
                if sums//number == root.val:
                    self.count += 1
                return (sums, number)
            
        ave(root)
            
        return self.count
                    
                    
                    
            
            
        