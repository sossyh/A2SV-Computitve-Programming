class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        visited = 0
        freq = Counter(s)
        stack = []
        
        for i in s:
            freq[i] -= 1
            if not (visited & 1 <<(ord(i))):
                while stack and freq[stack[-1]] >= 1 and stack[-1] >= i:
                    a = stack.pop()
                    visited ^= 1 <<(ord(a))
                
                stack.append(i)
                visited |= 1 <<(ord(i))
                
        
        return "".join(stack)