# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque()
        queue.append(root)
        
        while queue:
            leng = len(queue)
            ans = []
            for i in range(leng):
                item = queue.popleft()
                ans.append(item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            result.append(ans)
            
        return result
            
            
       