class Solution:
    def maxDepth(self, s: str) -> int:
        
        stack = []
        
        max_depth = 0
        
        for i in s:
            if not stack and i == "(":
                stack.append((i, 1))
            
            elif stack and i == "(":
                stack.append((i, stack[-1][1] + 1))
            
            if i == ")":
                max_depth = max(max_depth, len(stack))
                stack.pop()
            
        
        return max_depth
                