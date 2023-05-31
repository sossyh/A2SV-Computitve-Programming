# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def helper(root):
            if not root.right and not root.left:
                return root.val
            
            ans2, ans4, ans6 = 0, 0, 0
            if root.left:
                if root.left.left:
                    if root.left.left not in memo:
                        memo[root.left.left] = helper(root.left.left)
                    ans4 = memo[root.left.left]

                if root.left.right:
                    if root.left.right not in memo:
                        memo[root.left.right] = helper(root.left.right)
                    ans6 = memo[root.left.right]
                
                if root.left not in memo:
                    memo[root.left] = helper(root.left)
                ans2 = memo[root.left]


            ans1, ans3, ans5 = 0, 0, 0
            if root.right:
                if root.right.left:
                    if root.right.left not in memo:
                        memo[root.right.left] = helper(root.right.left)
                    ans3 = memo[root.right.left]

                if root.right.right:
                    if root.right.right not in memo:
                        memo[root.right.right] = helper(root.right.right)
                    ans5 = memo[root.right.right]

                if root.right not in memo:
                    memo[root.right] = helper(root.right)
                ans1 = memo[root.right]
            
            
            prevtotal = ans1 + ans2

            grandchild = ans3 + ans4 + ans5 + ans6

            return max(prevtotal, (grandchild + root.val))

        return helper(root)