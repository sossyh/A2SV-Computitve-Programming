class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        
        half = pow(2, n - 1) // 2
        
        if k <= half:
            return self.kthGrammar(n-1, k)
        else:
            newk = k - half
            return 1 - self.kthGrammar(n-1, newk)

        