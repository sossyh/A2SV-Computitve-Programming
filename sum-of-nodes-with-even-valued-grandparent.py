# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        visited = set()
        total = 0

        def dfs(vertex, parent = None, grandparent = None):
            nonlocal total
            if not vertex:
                return
                
            visited.add(vertex)
            if grandparent != None and grandparent.val % 2 == 0:
                    print(grandparent.val, vertex.val)
                    total += vertex.val
                
            if vertex.left not in visited:
                    dfs(vertex.left, vertex, parent)
            if vertex.right not in visited:
                    dfs(vertex.right, vertex, parent)
        
        dfs(root)
        
        return total