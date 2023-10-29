# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, node, to_delete, is_root):
        if not node:
            return
        
        if node.val in to_delete:
            self.dfs(node.left, to_delete, True)
            self.dfs(node.right, to_delete, True)
        else:
            if node.left:
                
                if node.left.val in to_delete:
                    self.dfs(node.left, to_delete, True)
                    node.left = None
                
                else:
                    self.dfs(node.left, to_delete, False)
            
            if node.right:
                if node.right.val in to_delete:
                    self.dfs(node.right, to_delete, True)
                    node.right = None
                
                else:
                    self.dfs(node.right, to_delete, False)
            
            if is_root:
                self.forest.append(node)
        
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        # tree and list which nodes to be deleted in the tree
        # after we delete the node both in the to delete list and in the tree we will be left with a forest, whcih  is have trees more than one
        # all the elements(nodes) in the tree and in to_delete are distnict
        # node values in the tree and lent todoelte <= 1000
        
        """
        what to do - traversing ove the tree
        
        - when i get the element to be dleted, i will make the child nodes of that elemnt (node) - root nodes
        - when i get to the node which is not in todelt this node should not delted so I will check the left and right childs of this node if both or one is in todelte, the relationshiiiiiiip between the currnode and the child node which is in to delete list should be cut-off
        - if it not i simply call my dsf fun

"""
        self.forest = []
        
        to_delete = set(to_delete)
        
        self.dfs(root, to_delete, True)
        
        return self.forest
        