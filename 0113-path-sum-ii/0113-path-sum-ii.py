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
        def find_path(root, total, summ ):
                total += root.val
                summ.append(root.val)
                
                if not root.left and not root.right:
                    if total == targetSum:
                        result.append(summ[:])
                    return
                
                if root.left:
                    find_path(root.left, total, summ)
                    summ.pop()
                
                if root.right:
                    find_path(root.right, total, summ)
                    summ.pop()
        
        find_path(root, 0, [])
        
        return result
        