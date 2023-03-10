# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
              
        def backTrack(lst, root):
            lst += str(root.val)
        
            if not root.left and not root.right:
                result.append(lst)
                return
            
            if root.left:
                backTrack(lst + "->", root.left)
            if root.right:
                backTrack(lst + "->", root.right)
                    
        backTrack("", root)
        return result
                    
                    
                
                