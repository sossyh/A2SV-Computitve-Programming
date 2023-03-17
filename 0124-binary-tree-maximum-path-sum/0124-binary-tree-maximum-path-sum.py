# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return root.val
        
        self.sums = float("-inf")
        
        def helper(root):
            if not root.left and not root.right:
                self.sums = max(self.sums, root.val)
                return root.val
            
            if root.left and root.right:
                lefts = max(helper(root.left), 0)
                rights = max(helper(root.right), 0)
                currsum = root.val + lefts + rights
                self.sums = max(self.sums, currsum, root.val)
                return max(currsum - lefts, currsum - rights)
            
            if root.left:
                lefts = max(helper(root.left), 0)
                currsum = root.val + lefts 
                self.sums = max(self.sums, currsum, root.val)
                return lefts + root.val
            
            if root.right:
                rights = max(helper(root.right), 0)
                currsum = root.val + rights
                self.sums = max(self.sums, currsum, root.val)
                return rights + root.val
        
        self.sums = max(helper(root), self.sums)
        
        return self.sums
            
                