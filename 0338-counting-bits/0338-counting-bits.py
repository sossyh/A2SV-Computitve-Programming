class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        
        for i in range(n+1):
            c = 0
            
            while i:
                if i & 1:
                    c += 1
                
                i = i >> 1
            
            result.append(c)
        
        return result