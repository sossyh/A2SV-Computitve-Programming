class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited = 0
        stack = []
        freq = Counter(s)
        
        for i in s:
            freq[i] -= 1
            if not visited & 1<<(ord(i)):
                while stack and stack[-1] >= i and freq[stack[-1]] > 0:
                    a = stack.pop()
                    visited ^= 1<<ord(a)
                
                stack.append(i)
                visited |= 1<<(ord(i))
        
        return "".join(stack)
        