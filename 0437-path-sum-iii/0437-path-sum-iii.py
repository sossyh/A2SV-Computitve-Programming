# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
      
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        
        self.count = 0
        prefix_dict = {0: 1}
        
        def traverse_tree(root, curr_total):
            
            
            if curr_total - targetSum in prefix_dict:
                self.count += prefix_dict[curr_total - targetSum]
            
            if curr_total not in prefix_dict:
                prefix_dict[curr_total] = 0
                       
            prefix_dict[curr_total] += 1
            
            if root.left:
                traverse_tree(root.left, curr_total + root.left.val)
            
            if root.right:
                traverse_tree(root.right, curr_total + root.right.val)
            
            prefix_dict[curr_total] -= 1
        
        traverse_tree(root, root.val)
        
        return self.count
            
            
                
            
            
                    
                
            
     