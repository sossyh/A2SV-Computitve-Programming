# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        d = collections.defaultdict(int)
        result = []
        
        def helper(root):
            lefts, rights = 0, 0
            if not root.left and not root.right:
                return root.val
            
            if root.left:
                lefts = helper(root.left) 
                d[lefts] += 1
            if root.right:
                rights = helper(root.right)
                d[rights] += 1
            
            return lefts + rights + root.val
        
        final = helper(root)
        d[final] += 1
        
        for item, freq in d.items():
            if freq == max(d.values()):
                result.append(item) 
        
        return result