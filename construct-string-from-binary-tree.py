# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root.right and not root.left:
            return str(root.val)
            
        result = str(root.val)

        def dfs(root):
            if not root.right and not root.left:
                return "(" + str(root.val) + ")"

            l, r = "()", ""
            if root.left:
                l = dfs(root.left)
            if root.right:
                r = dfs(root.right)
            
            return "(" + str(root.val) + str(l) + str(r) + ")"

        l, r = "()", ""
        if root.left:
            l = dfs(root.left)
        if root.right: 
            r = dfs(root.right)

        return result + l + r