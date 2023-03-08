# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q =[(root, 0, 0)]
        d = collections.defaultdict(list)
        
        while q:
            ans, row, col = q.pop()
            d[col].append((row, ans.val))
            if ans.left:
                q.append((ans.left, row+1, col-1))
            if ans.right:
                q.append((ans.right, row+1, col+1))
        for i in res:
            idx, val = i
            d[idx].append(val)
        d_sorted = sorted(d.items())
        
        ans = []
        for i in d_sorted:
            i[1].sort()
            temp = []
            for v in i[1]:
                temp.append(v[1])
            ans.append(temp)
            
        return ans
            
        
                
        