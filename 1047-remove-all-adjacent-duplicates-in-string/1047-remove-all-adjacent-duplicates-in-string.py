class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        
        for c in s:
            popped = None
            while stack and stack[-1] == c:
                popped = stack.pop()
            
            if c != popped:
                stack.append(c)
        
        return "".join(stack)
        