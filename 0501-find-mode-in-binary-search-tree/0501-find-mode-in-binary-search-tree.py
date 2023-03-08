# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = collections.defaultdict(int)
        queue = deque()
        queue.append(root)
        result = []
        
        while queue:
            item = queue.popleft()
            d[item.val] += 1
            if item.left:
                queue.append(item.left)
            if item.right:
                queue.append(item.right)
        
        for item, freq in d.items():
            if freq == max(d.values()):
                result.append(item)
        
        return result
        
        
        
        
        