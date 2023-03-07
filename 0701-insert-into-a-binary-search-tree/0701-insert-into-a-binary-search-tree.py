# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val)
        
        def insert(root,val):
            if not root:
                return 
            if root.left == None and val < root.val:
                root.left = TreeNode(val)
                return
            if root.right == None and val > root.val:
                root.right = TreeNode(val)
                return
            if val > root.val:
                insert(root.right, val)
            elif val < root.val:
                insert(root.left, val) 
                
        insert(root, val)
        
        return root