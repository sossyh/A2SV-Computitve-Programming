class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []
        
        for c in s:
            poped = None
            if stack and abs(ord(stack[-1]) - ord(c)) == 32:
                poped = stack.pop()
            
            if not poped:
                stack.append(c)
        
        
        return "".join(stack)