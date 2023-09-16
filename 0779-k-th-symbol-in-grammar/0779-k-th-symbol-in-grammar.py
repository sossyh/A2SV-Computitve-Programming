class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        a = self.kthGrammar(n-1, math.ceil(k/2))
        
        if a == 0 and k % 2 == 1:
            return 0
        
        elif a == 0 and k % 2 == 0:
            return 1
        
        elif a == 1 and k % 2 == 1:
            return 1
        
        else:
            return 0
            