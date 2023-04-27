# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        queue = deque()
        queue.append(root)
        result = []

        while queue:
            total = 0
            length = len(queue)
            for i in range(length):
                item = queue.popleft()
                total += item.val
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            
            result.append(total/length)
        
        return result