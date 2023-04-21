# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        string =  str(root.val)

        def dfs(root):
            nonlocal string
            if not root.right and not root.left:
                self.total += int(string)
                return

            if root.left:
                string += str(root.left.val)
                dfs(root.left)
                string = string[:-1]
            
            if root.right:
                string += str(root.right.val)
                dfs(root.right)
                string = string[:-1]
        
        dfs(root)
        
        return self.total