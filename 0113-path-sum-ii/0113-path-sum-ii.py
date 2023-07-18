# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
            
        result = []
        
        def path(root, candidates):
            candidates.append(root.val)
            if not root.left and not root.right:
                if sum(candidates) == targetSum:
                    result.append(candidates[:])
                print(candidates)
                # candidates.pop()
                return
            
            if root.left:
                path(root.left, candidates)
                candidates.pop()
            
            if root.right:
                path(root.right, candidates)
                candidates.pop()
            
        
        path(root, [])

        return result