class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        parent = self.kthGrammar(n - 1, math.ceil(k / 2))
        
        if parent == 0 and k % 2 == 1:
            return 0
        
        elif parent == 0 and k % 2 == 0:
            return 1
        
        elif parent == 1 and k % 2 == 1:
            return 1
        
        else:
            return 0