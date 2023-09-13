# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def areEqual(self, a, b):
        if not a and not b:
            return True
        
        if (not a.left and b.left) or (not a.right and b.right) or (not b.left and a.left) or (not b.right and a.right) or (a.val != b.val):
            return False
        
        return self.areEqual(a.left, b.left) and self.areEqual(a.right, b.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        queue = deque()
        queue.append(root)
        
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val:
                if self.areEqual(node, subRoot):
                    return True
            
            if node.left:
                queue.append(node.left)
            
            if node.right:
                queue.append(node.right)
        
        
        return False
            