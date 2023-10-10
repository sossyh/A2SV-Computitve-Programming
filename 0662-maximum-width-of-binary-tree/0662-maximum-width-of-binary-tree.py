# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        queue = deque()
        queue.append((root, 1))
        
        while queue:
            left_bound, right_bound = None, None
            
            for i in range(len(queue)):
                curr, curr_hori_idx = queue.popleft()
                
                if not left_bound and not right_bound:
                    left_bound, right_bound = curr_hori_idx, curr_hori_idx
                    
                left_bound = min(left_bound, curr_hori_idx)
                right_bound = max(right_bound, curr_hori_idx)
                
                if curr.left:
                    left_idx = curr_hori_idx * 2
                    queue.append((curr.left, left_idx))
                
                if curr.right:
                    right_idx = curr_hori_idx * 2 + 1
                    queue.append((curr.right, right_idx))
            
            max_width = max(max_width, right_bound - left_bound + 1)
        
        return max_width
                
        
       
        