class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        freq = Counter(s)
        visited = 0
        
        for c in s:
            freq[c] -= 1
            
            if visited & (1<<(ord(c))):
                continue
            
            while stack and freq[stack[-1]] > 0 and stack[-1] > c:
                a = stack.pop()
                visited ^= (1 << (ord(a)))

            stack.append(c)
            visited |= (1 << ord(c))
        
        
        return "".join(stack)
            