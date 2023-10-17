class Solution:
    def combination(self, tot, a):
        return factorial(tot) / (factorial(a) * factorial(tot - a))
    
    
    def uniquePaths(self, m: int, n: int) -> int:
        a = m - 1
        b = n - 1
        
        return int(self.combination(a+b, b))
           