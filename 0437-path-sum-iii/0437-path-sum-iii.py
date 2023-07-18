# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
      
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        d = {0:1}
        
        def helper(root, summ):
            if not root:
                return
            
            summ += root.val
                        
            if (summ - targetSum) in d:
                self.count += d[summ - targetSum]
            
            if summ not in d:
                d[summ] = 0
            d[summ] += 1
            
            helper(root.left, summ)
            helper(root.right, summ)
            
            d[summ] -= 1
        
        helper(root, 0)
        
        return self.count
            
            
                
            
            
                    
                
            
     