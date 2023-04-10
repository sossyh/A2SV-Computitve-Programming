class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        mapping = {
            '(':')',
            '[':']',
            '{':'}'            
        }
        
        for i in s:
            if i in mapping: 
                stack.append(i)
            elif stack and mapping[stack[-1]] == i:
                stack.pop()
            else:
                return False
        
        return stack == []

    
    