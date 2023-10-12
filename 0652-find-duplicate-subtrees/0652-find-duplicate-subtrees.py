# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = []
        duplicate = defaultdict(int)
        
        def postorder(root):
            if not root:
                return "n"
            
            interres = "#".join([postorder(root.left), postorder(root.right), str(root.val)])
            
            if duplicate[interres] == 1:
                result.append(root)
            
            duplicate[interres] += 1
            
            return interres
        
        postorder(root)
        
        return result
                