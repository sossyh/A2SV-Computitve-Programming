# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        
        def insert(tree, node):
            if node < tree.val and tree.left == None:
                tree.left = TreeNode(node)
                return
            
            if node > tree.val and tree.right == None:
                tree.right = TreeNode(node)
                return
            
            if node < tree.val:
                insert(tree.left, node)
            
            if node > tree.val:
                insert(tree.right, node)
            
        
        for i in preorder:
            insert(root, i)
        
        return root