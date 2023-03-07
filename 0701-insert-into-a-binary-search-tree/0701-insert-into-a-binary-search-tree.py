# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def insert(self, root, val):
        if root.left == None and root.val > val:
            root.left = TreeNode(val)
            return
        if root.right == None and root.val < val:
            root.right = TreeNode(val)
            return
        if root.val < val:
            self.insert(root.right, val)
        elif root.val > val:
            self.insert(root.left, val)
        
            
        
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        self.insert(root,val)
        return root
        
        