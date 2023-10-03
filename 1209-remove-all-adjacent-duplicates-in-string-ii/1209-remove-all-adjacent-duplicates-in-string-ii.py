class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        
        for i in range(len(s)):
            
            if stack and stack[-1][0] == s[i]:
                stack[-1] = (s[i], stack[-1][1] + 1)
            else:
                stack.append((s[i], 1))
           
            while stack and stack[-1][0] == s[i] and stack[-1][1] == k:
                stack.pop()
                poped = True
            
        
        result = ""
        
        for i in stack:
            result += i[0] * i[1]
        
        return result