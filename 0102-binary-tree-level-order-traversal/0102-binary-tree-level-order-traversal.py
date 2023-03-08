# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        
        result = []
        queue = []
        queue.append(root)
        
        while queue:
            length = len(queue)
            curr = []
            
            for i in range(length):
                ans = queue.pop(0)
                if ans.left:
                    queue.append(ans.left)
                if ans.right:
                    queue.append(ans.right)
                curr.append(ans.val)
            result.append(curr)
            
        return result
            
       